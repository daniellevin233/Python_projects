import os
import pickle

import data_loader
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

# ------------------------------------------- Constants ----------------------------------------

SEQ_LEN = 52
W2V_EMBEDDING_DIM = 300

ONEHOT_AVERAGE = "onehot_average"
W2V_AVERAGE = "w2v_average"
W2V_SEQUENCE = "w2v_sequence"

TRAIN = "train"
VAL = "val"
TEST = "test"
NEGATIVE_POLARITY = "neg"
RARE = "rare"

F = np.vectorize(data_loader.get_sentiment_class_from_val)


# ------------------------------------------ Helper methods and classes --------------------------

def get_available_device():
    """
    Allows training on GPU if available. Can help with running things faster when a GPU with cuda is
    available but not a most...
    Given a device, one can use module.to(device)
    and criterion.to(device) so that all the computations will be done on the GPU.
    """
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def save_pickle(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def save_model(model, path, epoch, optimizer):
    """
    Utility function for saving checkpoint of a model, so training or evaluation can be executed later on.
    :param model: torch module representing the model
    :param optimizer: torch optimizer used for training the module
    :param path: path to save the checkpoint into
    """
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict()}, path)


def load(model, path, optimizer):
    """
    Loads the state (weights, paramters...) of a model which was saved with save_model
    :param model: should be the same model as the one which was saved in the path
    :param path: path to the saved checkpoint
    :param optimizer: should be the same optimizer as the one which was saved in the path
    """
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    return model, optimizer, epoch


# ------------------------------------------ Data utilities ----------------------------------------

def load_word2vec():
    """ Load Word2Vec Vectors
        Return:
            wv_from_bin: All 3 million embeddings, each lengh 300
    """
    import gensim.downloader as api
    wv_from_bin = api.load("word2vec-google-news-300")
    vocab = list(wv_from_bin.vocab.keys())
    print(wv_from_bin.vocab[vocab[0]])
    print("Loaded vocab size %i" % len(vocab))
    return wv_from_bin


def create_or_load_slim_w2v(words_list, cache_w2v=False):
    """
    returns word2vec dict only for words which appear in the dataset.
    :param words_list: list of words to use for the w2v dict
    :param cache_w2v: whether to save locally the small w2v dictionary
    :return: dictionary which maps the known words to their vectors
    """
    w2v_path = "w2v_dict.pkl"
    if not os.path.exists(w2v_path):
        full_w2v = load_word2vec()
        w2v_emb_dict = {k: full_w2v[k] for k in words_list if k in full_w2v}
        if cache_w2v:
            save_pickle(w2v_emb_dict, w2v_path)
    else:
        w2v_emb_dict = load_pickle(w2v_path)
    return w2v_emb_dict


def get_w2v_average(sent, word_to_vec, embedding_dim):
    """
    This method gets a sentence and returns the average word embedding of the words consisting
    the sentence.
    :param sent: the sentence object
    :param word_to_vec: a dictionary mapping words to their vector embeddings
    :param embedding_dim: the dimension of the word embedding vectors
    :return The average embedding vector as numpy ndarray.
    """
    sent_to_emb = sentence_to_embedding(sent, word_to_vec, seq_len=1, embedding_dim=embedding_dim)
    return np.mean(sent_to_emb, axis=0)


def get_one_hot(size, ind):
    """
    this method returns a one-hot vector of the given size, where the 1 is placed in the ind entry.
    :param size: the size of the vector
    :param ind: the entry index to turn to 1
    :return: numpy ndarray which represents the one-hot vector
    """
    one_hot_vector = np.zeros(size, dtype=int)
    one_hot_vector[ind] = 1
    return one_hot_vector


def average_one_hots(sent : data_loader.Sentence, word_to_ind):
    """
    this method gets a sentence, and a mapping between words to indices, and returns the average
    one-hot embedding of the tokens in the sentence.
    :param sent: a sentence object.
    :param word_to_ind: a mapping between words to indices
    :return:
    """
    one_hot_vectors = np.zeros(shape=(len(sent.text), len(word_to_ind)))

    i = 0
    for word in sent.text:
        one_hot_vectors[i] = (get_one_hot(len(word_to_ind), word_to_ind[word]))
        i += 1

    result_vector_unnormalized = one_hot_vectors.sum(axis=0)
    return result_vector_unnormalized / len(sent.text)


def get_word_to_ind(words_list):
    """
    this function gets a list of words, and returns a mapping between
    words to their index.
    :param words_list: a list of words
    :return: the dictionary mapping words to the index
    """
    word_to_ind = {}
    counter = 0

    for word in words_list:
        if word not in word_to_ind.keys():
            word_to_ind[word] = counter
            counter += 1

    return word_to_ind


def sentence_to_embedding(sent, word_to_vec: dict, seq_len, embedding_dim=300):
    """
    this method gets a sentence and a word to vector mapping, and returns a list containing the
    words embeddings of the tokens in the sentence.
    :param sent: a sentence object
    :param word_to_vec: a word to vector mapping.
    :param seq_len: the fixed length for which the sentence will be mapped to.
    :param embedding_dim: the dimension of the w2v embedding
    :return: numpy ndarray of shape (seq_len, embedding_dim) with the representation of the sentence
    """
    embeddings = np.zeros(shape=(seq_len, embedding_dim))
    for i in range(min(len(sent.text), seq_len)):
        if sent.text[i] in word_to_vec:
            embeddings[i] = word_to_vec[sent.text[i]]
    return embeddings


class OnlineDataset(Dataset):
    """
    A pytorch dataset which generates model inputs on the fly from sentences of SentimentTreeBank
    """

    def __init__(self, sent_data, sent_func, sent_func_kwargs):
        """
        :param sent_data: list of sentences from SentimentTreeBank
        :param sent_func: Function which converts a sentence to an input datapoint
        :param sent_func_kwargs: fixed keyword arguments for the state_func
        """
        self.data = sent_data
        self.sent_func = sent_func
        self.sent_func_kwargs = sent_func_kwargs

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sent = self.data[idx]
        sent_emb = self.sent_func(sent, **self.sent_func_kwargs)
        sent_label = sent.sentiment_class
        return sent_emb, sent_label


class DataManager():
    """
    Utility class for handling all data management task. Can be used to get iterators for training and
    evaluation.
    """

    def __init__(self, data_type=ONEHOT_AVERAGE, use_sub_phrases=True, dataset_path="stanfordSentimentTreebank", batch_size=50,
                 embedding_dim=None):
        """
        builds the data manager used for training and evaluation.
        :param data_type: one of ONEHOT_AVERAGE, W2V_AVERAGE and W2V_SEQUENCE
        :param use_sub_phrases: if true, training data will include all sub-phrases plus the full sentences
        :param dataset_path: path to the dataset directory
        :param batch_size: number of examples per batch
        :param embedding_dim: relevant only for the W2V data types.
        """

        # load the dataset
        self.sentiment_dataset = data_loader.SentimentTreeBank(dataset_path, split_words=True)
        # map data splits to sentences lists
        self.sentences = {}
        self.sentences[NEGATIVE_POLARITY] = [self.sentiment_dataset.sentences[i]
                                            for i in data_loader.get_negated_polarity_examples(self.sentiment_dataset.sentences)]
        self.sentences[RARE] = [self.sentiment_dataset.sentences[i]
                                            for i in data_loader.get_rare_words_examples(self.sentiment_dataset.sentences, self.sentiment_dataset, 50)]
        if use_sub_phrases:
            self.sentences[TRAIN] = self.sentiment_dataset.get_train_set_phrases()
        else:
            self.sentences[TRAIN] = self.sentiment_dataset.get_train_set()

        self.sentences[VAL] = self.sentiment_dataset.get_validation_set()
        self.sentences[TEST] = self.sentiment_dataset.get_test_set()

        # map data splits to sentence input preperation functions
        words_list = list(self.sentiment_dataset.get_word_counts().keys())
        if data_type == ONEHOT_AVERAGE:
            self.sent_func = average_one_hots
            self.sent_func_kwargs = {"word_to_ind": get_word_to_ind(words_list)}
        elif data_type == W2V_SEQUENCE:
            self.sent_func = sentence_to_embedding

            self.sent_func_kwargs = {"seq_len": SEQ_LEN,
                                     "word_to_vec": create_or_load_slim_w2v(words_list),
                                     "embedding_dim": embedding_dim
                                     }
        elif data_type == W2V_AVERAGE:
            self.sent_func = get_w2v_average
            words_list = list(self.sentiment_dataset.get_word_counts().keys())
            self.sent_func_kwargs = {"word_to_vec": create_or_load_slim_w2v(words_list),
                                     "embedding_dim": embedding_dim
                                     }
        else:
            raise ValueError("invalid data_type: {}".format(data_type))
        # map data splits to torch datasets and iterators
        self.torch_datasets = {k: OnlineDataset(sentences, self.sent_func, self.sent_func_kwargs) for
                               k, sentences in self.sentences.items()}
        self.torch_iterators = {k: DataLoader(dataset, batch_size=batch_size, shuffle=k == TRAIN)
                                for k, dataset in self.torch_datasets.items()}


    def get_torch_iterator(self, data_subset=TRAIN):
        """
        :param data_subset: one of TRAIN VAL and TEST
        :return: torch batches iterator for this part of the dataset
        """
        return self.torch_iterators[data_subset]

    def get_labels(self, data_subset=TRAIN):
        """
        :param data_subset: one of TRAIN VAL and TEST
        :return: numpy array with the labels of the requested part of the datset in the same order of the
        examples.
        """
        return np.array([sent.sentiment_class for sent in self.sentences[data_subset]])

    def get_input_shape(self):
        """
        :return: the shape of a single example from this dataset (only of x, ignoring y the label).
        """
        return self.torch_datasets[TRAIN][0][0].shape


# ------------------------------------ Models ----------------------------------------------------

class LSTM(nn.Module):
    """
    An LSTM for sentiment analysis with architecture as described in the exercise description.
    """
    def __init__(self, embedding_dim, hidden_dim, n_layers, dropout):
        super().__init__()
        self.LSTM = nn.LSTM(input_size=embedding_dim, hidden_size=hidden_dim,
                num_layers=n_layers, bidirectional=True)
        self.dropout = nn.Dropout(p=dropout)
        self.linear = nn.Linear(in_features=2*hidden_dim, out_features=1)

    def forward(self, text):
        result = self.LSTM(text)
        drop = self.dropout(result[0][:,-1,:])
        out = self.linear(drop)
        return out

    def predict(self, text):
        result = self.LSTM(text)
        drop = self.dropout(result[0][:,-1,:])
        linear = self.linear(drop)
        out = nn.Sigmoid()(linear)
        return out


class LogLinear(nn.Module):
    """
    general class for the log-linear models for sentiment analysis.
    """
    def __init__(self, embedding_dim):
        super().__init__()
        self.linear = nn.Linear(in_features=embedding_dim, out_features=1)

    def forward(self, x):
        return self.linear(x)

    def predict(self, x):
        h1 = self.linear(x)
        out = nn.Sigmoid()(h1)
        return out


# ------------------------- training functions -------------


def binary_accuracy(preds, y):
    """
    This method returns tha accuracy of the predictions, relative to the labels.
    You can choose whether to use numpy arrays or tensors here.
    :param preds: a vector of predictions
    :param y: a vector of true labels
    :return: scalar value - (<number of accurate predictions> / <number of examples>)
    """
    return np.sum(F(preds) == F(y)) / y.shape[0]


def train_epoch(model, data_iterator, optimizer, criterion : nn.BCEWithLogitsLoss):
    """
    This method operates one epoch (pass over the whole train set) of training of the given model,
    and returns the accuracy and loss for this epoch
    :param model: the model we're currently training
    :param data_iterator: an iterator, iterating over the training data for the model.
    :param optimizer: the optimizer object for the training process.
    :param criterion: the criterion object for the training process.
    """
    model.train()

    accuracies = []
    losses = []
    for batch in data_iterator:
        optimizer.zero_grad()
        pred = model.forward(batch[0].view(tuple(batch[0].size())).float())

        accuracies.append(binary_accuracy(pred.data.numpy().reshape(pred.shape[0]),
                                          batch[1].data.numpy().reshape(batch[1].shape[0])))

        loss = criterion(pred, batch[1].view(batch[1].shape[0], 1).float())
        losses.append(loss.item())
        loss.backward()
        optimizer.step()

    return np.mean(accuracies), np.mean(losses)


def evaluate(model, data_iterator, criterion):
    """
    evaluate the model performance on the given data
    :param model: one of our models..
    :param data_iterator: torch data iterator for the relevant subset
    :param criterion: the loss criterion used for evaluation
    :return: tuple of (average loss over all examples, average accuracy over all examples)
    """
    model.eval()

    accuracies = []
    losses = []
    for batch in data_iterator:
        pred = model.predict(batch[0].view(tuple(batch[0].size())).float())

        accuracies.append(binary_accuracy(pred.data.numpy().reshape(pred.shape[0]),
                                          batch[1].data.numpy().reshape(batch[1].shape[0])))

        loss = criterion(pred, batch[1].view(batch[1].shape[0], 1).float())
        losses.append(loss.item())

    return np.mean(accuracies), np.mean(losses)


def get_predictions_for_data(model, data_iter):
    """

    This function should iterate over all batches of examples from data_iter and return all of the models
    predictions as a numpy ndarray or torch tensor (or list if you prefer). the prediction should be in the
    same order of the examples returned by data_iter.
    :param model: one of the models you implemented in the exercise
    :param data_iter: torch iterator as given by the DataManager
    :return:
    """
    predicts = []
    for batch in data_iter:
        predicts.append(model.predict(batch[0]))
    return torch.tensor(predicts)


def train_model(model, data_manager: DataManager, n_epochs, lr, weight_decay=0.):
    """
    Runs the full training procedure for the given model. The optimization should be done using the Adam
    optimizer with all parameters but learning rate and weight decay set to default.
    :param model: module of one of the models implemented in the exercise
    :param data_manager: the DataManager object
    :param n_epochs: number of times to go over the whole training set
    :param lr: learning rate to be used for optimization
    :param weight_decay: parameter for l2 regularization
    """
    optimizer = torch.optim.Adam(params=model.parameters(), lr=lr, weight_decay=weight_decay)
    train_losses = np.zeros(n_epochs)
    train_accuracies = np.zeros(n_epochs)
    val_losses = np.zeros(n_epochs)
    val_accuracies = np.zeros(n_epochs)

    for i in range(n_epochs):
        train_acc, train_loss = train_epoch(model, data_manager.get_torch_iterator(data_subset=TRAIN),
                                     optimizer, nn.BCEWithLogitsLoss())
        train_losses[i] = train_loss
        train_accuracies[i] = train_acc
        val_acc, val_loss = evaluate(model, data_manager.get_torch_iterator(data_subset=VAL),
                                            nn.BCEWithLogitsLoss())
        val_losses[i] = val_loss
        val_accuracies[i] = val_acc

    return train_losses, val_losses, train_accuracies, val_accuracies, optimizer


def plot_function_of_epochs(train_values, val_values, ylabel: str, embedding_name: str, weight_decay, n_epochs=20):
    plt.grid(), plt.title(ylabel.capitalize() + " for " + embedding_name +
                          " with weight_decay = " + str(weight_decay))
    plt.xlabel("Epoch"), plt.ylabel(ylabel.capitalize() + " value")
    plt.plot(np.arange(1, n_epochs + 1), train_values, label="Train " + ylabel, color='k')
    plt.plot(np.arange(1, n_epochs + 1), val_values, label="Validation " + ylabel, color='g')
    plt.legend(loc='best')
    plt.savefig(os.getcwd() + '/{0}_{1}_{2}.png'.format(embedding_name, ylabel, weight_decay))
    plt.show()


def train_log_linear_with_one_hot():
    """
    Here comes your code for training and evaluation of the log linear model with one hot representation.
    """
    data_manager = DataManager(data_type=ONEHOT_AVERAGE)

    max_val_acc = 0
    best_weight_dec = 0
    models = {}
    for weight_dec in [0, 0.001, 0.0001]:
        model = LogLinear(embedding_dim=data_manager.get_input_shape()[0])
        train_losses, val_losses, train_accuracies, val_accuracies, optimizer = \
            train_model(model, data_manager, n_epochs=20, lr=0.01, weight_decay=weight_dec)
        plot_function_of_epochs(train_losses, val_losses, "loss", "onehot embedding",  weight_dec)
        plot_function_of_epochs(train_accuracies, val_accuracies, "accuracy", "onehot embedding", weight_dec)
        models[weight_dec] = (model, optimizer)

        if val_accuracies[-1] > max_val_acc:
            best_weight_dec = weight_dec
            max_val_acc = val_accuracies[-1]

    save_model(models[best_weight_dec][0], os.getcwd() + '/log_linear/best_model.pkl',
               20, models[best_weight_dec][1])

    test_acc, test_loss = \
        evaluate(models[best_weight_dec][0], data_manager.get_torch_iterator(data_subset=TEST), nn.BCEWithLogitsLoss())
    with open(os.getcwd() + '/log_linear/test_results.txt', 'w') as results_file:
        results_file.write('Test accuracy: {0}\n'.format(test_acc))
        results_file.write('Test loss: {0}\n'.format(test_loss))
        results_file.write('Weight dec: {0}\n'.format(best_weight_dec))
    return


def train_log_linear_with_w2v():
    """
    Here comes your code for training and evaluation of the log linear model with word embeddings
    representation.
    """
    data_manager = DataManager(data_type=W2V_AVERAGE, embedding_dim=W2V_EMBEDDING_DIM)

    max_val_acc = 0
    best_weight_dec = 0
    models = {}
    for weight_dec in [0, 0.001, 0.0001]:
        model = LogLinear(embedding_dim=data_manager.get_input_shape()[0])
        train_losses, val_losses, train_accuracies, val_accuracies, optimizer = \
            train_model(model, data_manager, n_epochs=20, lr=0.01, weight_decay=weight_dec)
        plot_function_of_epochs(train_losses, val_losses, "loss", "word2vec embedding", weight_dec)
        plot_function_of_epochs(train_accuracies, val_accuracies, "accuracy", "word2vec embedding", weight_dec)
        models[weight_dec] = (model, optimizer)

        if val_accuracies[-1] > max_val_acc:
            best_weight_dec = weight_dec
            max_val_acc = val_accuracies[-1]

    save_model(models[best_weight_dec][0], os.getcwd() + '/word2vec/best_model.pkl',
               20, models[best_weight_dec][1])

    test_acc, test_loss = \
        evaluate(models[best_weight_dec][0], data_manager.get_torch_iterator(data_subset=TEST), nn.BCEWithLogitsLoss())
    with open(os.getcwd() + '/word2vec/test_results.txt', 'w') as results_file:
        results_file.write('Test accuracy: {0}\n'.format(test_acc))
        results_file.write('Test loss: {0}\n'.format(test_loss))
        results_file.write('Weight dec: {0}\n'.format(best_weight_dec))
    return


def train_lstm_with_w2v():
    """
    Here comes your code for training and evaluation of the LSTM model.
    """
    data_manager = DataManager(data_type=W2V_SEQUENCE, embedding_dim=W2V_EMBEDDING_DIM)

    weight_dec = 0.0001
    model = LSTM(embedding_dim=data_manager.get_input_shape()[1], hidden_dim=100, n_layers=1, dropout=0.5)
    train_losses, val_losses, train_accuracies, val_accuracies, optimizer = \
        train_model(model, data_manager, n_epochs=4, lr=0.001, weight_decay=weight_dec)
    plot_function_of_epochs(train_losses, val_losses, "loss", "lstm network", weight_dec, n_epochs=4)
    plot_function_of_epochs(train_accuracies, val_accuracies, "accuracy", "lstm network", weight_dec, n_epochs=4)

    save_model(model, os.getcwd() + '/lstm/best_model.pkl'.format(weight_dec),
               20, optimizer)

    test_acc, test_loss = \
        evaluate(model, data_manager.get_torch_iterator(data_subset=TEST), nn.BCEWithLogitsLoss())
    with open(os.getcwd() + '/lstm/test_results.txt', 'w') as results_file:
        results_file.write('Test accuracy: {0}\n'.format(test_acc))
        results_file.write('Test loss: {0}\n'.format(test_loss))
        results_file.write('Weight dec: {0}\n'.format(weight_dec))
    return


def check_subsets_results():
    log_linear_data_manager = DataManager(data_type=ONEHOT_AVERAGE)
    log_linear_model = LogLinear(embedding_dim=log_linear_data_manager.get_input_shape()[0])
    log_linear_optimizer = torch.optim.Adam(params=log_linear_model.parameters(), lr=0.01, weight_decay=0)
    log_linear_model, log_linear_optimizer, epoch = \
        load(log_linear_model, 'log_linear/best_model.pkl', log_linear_optimizer)
    log_linear_pol_loss, log_linear_pol_acc = evaluate(log_linear_model,
              log_linear_data_manager.get_torch_iterator(data_subset=NEGATIVE_POLARITY), nn.BCEWithLogitsLoss())
    log_linear_rar_loss, log_linear_rar_acc = evaluate(log_linear_model,
                                                       log_linear_data_manager.get_torch_iterator(
                                                           data_subset=RARE), nn.BCEWithLogitsLoss())
    print("One Hot Log Linear")
    print("Polarity: loss: {0}, acc: {1}".format(log_linear_pol_loss, log_linear_pol_acc))
    print("Rare: loss: {0}, acc: {1}".format(log_linear_rar_loss, log_linear_rar_acc))

    word2vec_data_manager = DataManager(data_type=W2V_AVERAGE, embedding_dim=W2V_EMBEDDING_DIM)
    word2vec_model = LogLinear(embedding_dim=word2vec_data_manager.get_input_shape()[0])
    word2vec_optimizer = torch.optim.Adam(params=word2vec_model.parameters(), lr=0.01, weight_decay=0)
    word2vec_model, word2vec_optimizer, epoch = \
        load(word2vec_model, 'word2vec/best_model.pkl', word2vec_optimizer)
    word2vec_pol_loss, word2vec_pol_acc = evaluate(word2vec_model,
                                                       word2vec_data_manager.get_torch_iterator(
                                                           data_subset=NEGATIVE_POLARITY), nn.BCEWithLogitsLoss())
    word2vec_rar_loss, word2vec_rar_acc = evaluate(word2vec_model,
                                                       word2vec_data_manager.get_torch_iterator(
                                                           data_subset=RARE), nn.BCEWithLogitsLoss())
    print("Word2Vec")
    print("Polarity - loss: {0}, acc: {1}".format(word2vec_pol_loss, word2vec_pol_acc))
    print("Rare - loss: {0}, acc: {1}".format(word2vec_rar_loss, word2vec_rar_acc))

    lstm_data_manager = DataManager(data_type=W2V_SEQUENCE, embedding_dim=W2V_EMBEDDING_DIM)
    lstm_model = LSTM(embedding_dim=lstm_data_manager.get_input_shape()[1], hidden_dim=100, n_layers=1, dropout=0.5)
    lstm_optimizer = torch.optim.Adam(params=lstm_model.parameters(), lr=0.001, weight_decay=0.0001)
    lstm_model, lstm_optimizer, epoch = \
        load(lstm_model, 'lstm/best_model.pkl', lstm_optimizer)
    lstm_pol_loss, lstm_pol_acc = evaluate(lstm_model,
                                                   lstm_data_manager.get_torch_iterator(
                                                       data_subset=NEGATIVE_POLARITY), nn.BCEWithLogitsLoss())
    lstm_rar_loss, lstm_rar_acc = evaluate(lstm_model,
                                                   lstm_data_manager.get_torch_iterator(
                                                       data_subset=RARE), nn.BCEWithLogitsLoss())
    print("LSTM")
    print("Polarity - loss: {0}, acc: {1}".format(lstm_pol_loss, lstm_pol_acc))
    print("Rare - loss: {0}, acc: {1}".format(lstm_rar_loss, lstm_rar_acc))


if __name__ == '__main__':
    # train_log_linear_with_one_hot()
    # train_log_linear_with_w2v()
    # train_lstm_with_w2v()
    check_subsets_results()
