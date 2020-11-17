from keras import models
from plot import plot_and_save
import pandas as pd
from neural_network import NeuralNetwork
from sentiment_analysis_data import SentimentAnalysisData
from activate_gpu import activate_gpu
import platform, sys

"""
Schema:
    
  | Unnamed: 0 | count | hate_speech | offensive_language | neither | class | tweet |
    
  0 - hate speech - 1430 samples 
  1 - offensive language - 19190 samples
  2 - neither - 4163 - samples
"""

# paths constants #
DATA_PATH = './data/labeled_data.csv'
PLOTS_PATH = './plt/{}.png'

# model constants #
NUM_OF_CLASSES = 3

# data partition constants #
TRAIN_RATIO, VAL_RATIO, TEST_RATIO = 0.8, 0.1, 0.1 # must sum up to 1.

# THRESHOLD tuning constants #

# threshold represents the minimal frequency
# that a word has to appear in order to be included in the vocabulary
THRESHOLD_WORDS_OPT = 8
TUNING_THRESHOLD = False # TODO turn to False
THRESHOLDS = [t for t in range(4, 13, 1)]

# non-final layers tuning constants #
INTERMEDIATE_LAYERS_N_OPT = 3
TUNING_LAYERS = False # TODO turn to False
NUMS_OF_LAYERS = range(1, 10)

# num of nodes tuning constants #
NUM_OF_NODES_PER_LAYER_OPT = 16
TUNING_NODES = False # TODO turn to False
NUMS_OF_NODES = [pow(2, i) for i in range(2, 7)]

# epochs tuning constants #
EPOCHS_OPT = 6
TUNING_EPOCHS = False # TODO turn to False

# layers architecture parameters #
ACTIVATION_FUNCTIONS_OPT = ('relu',) * INTERMEDIATE_LAYERS_N_OPT + ('softmax',)
NODES_BY_LAYER_OPT = (NUM_OF_NODES_PER_LAYER_OPT,) * INTERMEDIATE_LAYERS_N_OPT + (NUM_OF_CLASSES,)

# dropout parameters #
DROPOUT_RATES = (0.2,) * INTERMEDIATE_LAYERS_N_OPT

# k-fold validation constants #
FOLDS_K = 4
K_FOLD_TRAIN_SIZE = 20000
K_FOLD_VALIDATION = False # TODO

def tune_threshold(path):
    """
    Tries different thresholds from THRESHOLDS, builds and fits a model for each of them
    and saves two plots - one for loss change and one for accuracy change - both as functions
    of threshold
    :param path: path to read the data from
    """
    res_loss, res_val_loss, res_acc, res_val_acc = [], [], [], []
    for threshold in THRESHOLDS:
        d = pd.read_csv(path)
        d = SentimentAnalysisData(x=d['tweet'],
                                  y=d['class'],
                                  test_ratio=TEST_RATIO,
                                  val_ratio=VAL_RATIO,
                                  threshold=threshold)
        nn = network_exe(d)
        loss_history = nn.get_loss_history()
        res_loss.append(loss_history[0][-1])
        res_val_loss.append(loss_history[1][-1])
        accuracy_history = nn.get_accuracy_history()
        res_acc.append(accuracy_history[0][-1])
        res_val_acc.append(accuracy_history[1][-1])

    plot_and_save(THRESHOLDS, [res_loss, res_val_loss], PLOTS_PATH.format('thresholds_loss'),
                  labels=['Training loss', 'Validation loss'], title='Loss change on threshold tuning',
                  x_label='Threshold', y_label='Loss')

    plot_and_save(THRESHOLDS, [res_acc, res_val_acc], PLOTS_PATH.format('thresholds_accuracy'),
                  labels=['Training accuracy', 'Validation accuracy'], title='Accuracy change on threshold tuning',
                  x_label='Threshold', y_label='Accuracy', ylim=(0.7, 1))


def tune_num_of_layers(path):
    """
    Tries different numbers of layers from NUMS_OF_LAYERS range object,
    builds and fits a model for each of them and saves two plots -
    one for loss change and one for accuracy change - both as functions of number of layers
    :param path: path to read the data from
    """
    res_loss, res_val_loss, res_acc, res_val_acc = [], [], [], []
    data = load_data(path)
    for i in NUMS_OF_LAYERS:
        activation_functions_configs = ['relu'] * i + ['softmax']
        nodes_by_layer_configs = [NUM_OF_NODES_PER_LAYER_OPT] * i + [NUM_OF_CLASSES]
        nn = network_exe(data, activation_functions=activation_functions_configs,
                               nodes_by_layer=nodes_by_layer_configs)
        loss_history = nn.get_loss_history()
        res_loss.append(loss_history[0][-1])
        res_val_loss.append(loss_history[1][-1])
        accuracy_history = nn.get_accuracy_history()
        res_acc.append(accuracy_history[0][-1])
        res_val_acc.append(accuracy_history[1][-1])

    plot_and_save(NUMS_OF_LAYERS, [res_loss, res_val_loss], PLOTS_PATH.format('layers_loss'),
                  labels=['Training loss', 'Validation loss'], title='Loss change on layers tuning',
                  x_label='Number of used layers', y_label='Loss')

    plot_and_save(NUMS_OF_LAYERS, [res_acc, res_val_acc], PLOTS_PATH.format('layers_accuracy'),
                  labels=['Training accuracy', 'Validation accuracy'], title='Accuracy change on layers tuning',
                  x_label='Number of used layers', y_label='Accuracy', ylim=(0.7, 1))


def tune_num_of_nodes(path):
    """
    Tries different numbers of nodes per layer from NUMS_OF_NODES iterable,
    builds and fits a model for each of them and saves two plots -
    one for loss change and one for accuracy change - both as functions of number of nodes per layer
    :param path: path to read the data from
    """
    res_loss, res_val_loss, res_acc, res_val_acc = [], [], [], []
    data = load_data(path)
    for i in NUMS_OF_NODES:
        nodes_by_layer_configs = [i] * INTERMEDIATE_LAYERS_N_OPT + [NUM_OF_CLASSES]
        nn = network_exe(data, nodes_by_layer=nodes_by_layer_configs)
        loss_history = nn.get_loss_history()
        res_loss.append(loss_history[0][-1])
        res_val_loss.append(loss_history[1][-1])
        accuracy_history = nn.get_accuracy_history()
        res_acc.append(accuracy_history[0][-1])
        res_val_acc.append(accuracy_history[1][-1])

    plot_and_save(NUMS_OF_NODES, [res_loss, res_val_loss], PLOTS_PATH.format('nodes_loss'),
                  labels=['Training loss', 'Validation loss'], title='Loss change on number of nodes tuning',
                  x_label='Number of nodes per layer', y_label='Loss')

    plot_and_save(NUMS_OF_NODES, [res_acc, res_val_acc], PLOTS_PATH.format('nodes_accuracy'),
                  labels=['Training accuracy', 'Validation accuracy'], title='Accuracy change on number of nodes tuning',
                  x_label='Number of nodes per layer', y_label='Accuracy', ylim=(0.7, 1))


def tune_epochs(path):
    """
    Build and fit network on currently set optimal epochs number and save two plots -
    one for loss change and one for accuracy change - both as functions of epoch.
    :param path: path to read the data from
    """
    data = load_data(path)
    nn = network_exe(data)

    loss_history = nn.get_loss_history()
    accuracy_history = nn.get_accuracy_history()

    plot_and_save(range(1, len(loss_history[0]) + 1), loss_history, PLOTS_PATH.format('epochs_loss'),
                  labels=['Training loss', 'Validation loss'], title='Training and validation loss to epochs',
                  x_label='Epochs', y_label='Loss')

    plot_and_save(range(1, len(loss_history[0]) + 1), accuracy_history, PLOTS_PATH.format('epochs_accuracy'),
                  labels=['Training accuracy', 'Validation accuracy'],
                  title='Training and validation accuracy to epochs',
                  x_label='Epochs', y_label='Accuracy')


def load_data(path, k_fold=0):
    '''
    Load data from passed csv file and generate a Data object
    :param path: path of the csv file to be loaded
    :return: new Data object
    '''
    d = pd.read_csv(path)
    # extracting relevant columns from the data, tweets are input data (independent variable),
    # classes are output data (labels or dependent variable)
    return SentimentAnalysisData(x=d['tweet'],
                                 y=d['class'],
                                 test_ratio=TEST_RATIO,
                                 val_ratio=VAL_RATIO,
                                 threshold=THRESHOLD_WORDS_OPT,
                                 k_fold=k_fold)


def network_exe(data, activation_functions=ACTIVATION_FUNCTIONS_OPT, nodes_by_layer=NODES_BY_LAYER_OPT,
                epochs=EPOCHS_OPT, droupout_rates=DROPOUT_RATES):
    """
    Build, compile and train a neural network
    :param data: data to feed the network
    :return: fitted neural network
    """
    nn = NeuralNetwork(data=data,
                       model=models.Sequential(),
                       activation_functions=activation_functions,
                       nodes_by_layer=nodes_by_layer,
                       optimizer='rmsprop',
                       metrics=['accuracy'],  # metrics.AUC()], #metrics.Precision(), metrics.Recall()],
                       loss='categorical_crossentropy',
                       dropout_rates=droupout_rates)
    nn.build()
    nn.fit(epochs=epochs, batch_size=256)
    return nn


def sentiment_analysis_k_fold(path):
    d = pd.read_csv(path)
    data = SentimentAnalysisData(x=d['tweet'],
                                 y=d['class'],
                                 test_ratio=(1 - (K_FOLD_TRAIN_SIZE / len(d['tweet']))),
                                 threshold=THRESHOLD_WORDS_OPT,
                                 k_fold=FOLDS_K)
    nn = network_exe(data)
    print("K-fold Validation score [loss, accuracy]: ", nn.validation_score)
    nn.evaluate()


def sentiment_analysis():
    # some versions of GPU on windows do not activate with keras automatically
    if (platform.system() == 'Windows'):
        # print("GPU isn't activated!!!")
        activate_gpu() # TODO decomment when training

    try:
        if(TUNING_THRESHOLD):
            tune_threshold(DATA_PATH)
        elif(TUNING_LAYERS):
            tune_num_of_layers(DATA_PATH)
        elif(TUNING_NODES):
            tune_num_of_nodes(DATA_PATH)
        elif(TUNING_EPOCHS):
            tune_epochs(DATA_PATH)
        else:
            if(K_FOLD_VALIDATION):
                sentiment_analysis_k_fold(DATA_PATH)
            else:
                data = load_data(DATA_PATH)
                nn = network_exe(data)
                nn.evaluate()

    except FileNotFoundError as err:
        print(err.strerror)
        exit()

# TODO modify tuning plots by introducing third dimension (epoch, score, hyperparameter)

def query_yes_no(question, default=None):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if __name__ == '__main__':
    if query_yes_no("Would you like to use k-fold validation?"):
        K_FOLD_VALIDATION = True
    sentiment_analysis()
