from copy import deepcopy


class Unigram:
    def __init__(self, train_samples):
        self.__train_set = train_samples
        self.__word_to_best_tag = dict.fromkeys([sample[0] for sample in train_samples])

    def train(self):
        """
        Train unigram HMM model based on nd array containing
        all the samples of form:
                                [('word1', 'tag1'), ('word2', 'tag2'),...],
        resulting in initialization of dictionary of words mapped to the most
        frequent tag in the train they appeared with:
                                                     {'word1': 'NN', 'word2': 'JJ', ...}
        """
        #  init dict of all possible tags: {'NN': 0, 'JJ': 0,...}
        tags_count_dict = dict.fromkeys([sample[1] for sample in self.__train_set], 0)

        #  init dict of all possible words to their tags in the training set:
        #  {'word1': {'NN': 0, 'JJ': 0,...},
        #   'word2': {'NN': 0, 'JJ': 0,...},...
        word_to_dict_of_tags = dict.fromkeys([sample[0] for sample in self.__train_set])
        for key in word_to_dict_of_tags:
            word_to_dict_of_tags[key] = deepcopy(tags_count_dict)

        #  count tags for every word:
        #  {'word1': {'NN': 3, 'JJ': 1,...},
        #   'word2': {'NN': 0, 'JJ': 9,...},...
        for sample in self.__train_set:
            word_to_dict_of_tags[sample[0]][sample[1]] += 1

        #  fill dict which determines the most frequent tagging for each word in training set
        #  {'word1': 'NN', // when 'NN' is the most frequent tag for 'word1' according to train
        #  {'word2': 'JJ', // when 'JJ' is the most frequent tag for 'word2' according to train
        for word, dict_of_tags in word_to_dict_of_tags.items():
            self.__word_to_best_tag[word] = max(dict_of_tags, key=dict_of_tags.get)

    def predict(self, token):
        """
        Predict POS tag for given token using MLE for unigram HMM model,
        with constant 'NN' tag for unknown words
        :param token: word to be labeled
        :return: predicted label
        """
        if token in self.__word_to_best_tag:
            return self.__word_to_best_tag[token]
        return 'NN'

    def get_accuracy_rate(self, test_set):
        error_cnt = 0
        for sample in test_set:
            if self.predict(sample[0]) != sample[1]:
                error_cnt += 1
        return 1 - error_cnt / len(test_set)
