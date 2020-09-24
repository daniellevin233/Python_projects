from collections import Counter
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
from numpy import random


class Bigram:
    def __init__(self, train_sentences, smoothing_coef=0):
        self.__train_set = train_sentences
        self.__possible_tags = set()
        self.__train_words = set()
        self.__train_samples = list()
        self.__transition_df = None
        self.__emission_df = None
        self.__tags_count_dict_normalized = None
        self.__smooth_coef = smoothing_coef

    def train(self):
        for sentence in self.__train_set:
            for sample in sentence:
                self.__train_samples.append(sample)
                self.__train_words.add(sample[0])
                self.__possible_tags.add(sample[1])
        tags_count_dict = Counter([sample[1] for sample in self.__train_samples])
        num_of_tags = sum(tags_count_dict.values())
        self.__tags_count_dict_normalized = {tag: cnt / num_of_tags for tag, cnt in tags_count_dict.items()}
        self.__transition_df = self.get_transition_df()
        self.__emission_df = self.get_emission_df()

    def get_accuracy_rate(self, test_sentences):
        error = 0
        num_of_all_words = 0
        for sentence in test_sentences:
            words = []
            true_labeling = []
            for sample in sentence:
                words.append(sample[0])
                true_labeling.append(sample[1])
            prediction = self.predict(words)
            num_of_all_words += len(prediction)
            for i in range(len(true_labeling)):
                if prediction[i] != true_labeling[i]:
                    error += 1
        return 1 - (error / num_of_all_words)

    def get_confusion_matrix(self, test_sentences):
        predictions = []
        true_labels = []
        for sentence in test_sentences:
            words = []
            true_labeling = []
            for sample in sentence:
                words.append(sample[0])
                true_labeling.append(sample[1])
            predictions += self.predict(words)
            true_labels += true_labeling
        return confusion_matrix(true_labels, predictions)

    def predict(self, sentence):
        START = '*'
        tags_lst = list(self.__possible_tags)
        sentence = [START] + sentence
        dynamic_table = np.zeros(shape=(len(tags_lst), len(sentence)), dtype=np.float64)
        dynamic_table[:, 0] = 1

        tags_MLE = list()  # loop on columns of the dataframe, word contains name of the column, col contains its values
        for i, prev_word, cur_word in zip(range(1, len(sentence)), sentence[:-1], sentence[1:]):
            if cur_word not in self.__train_words:
                # if the word is unknown, assign tag assuming the distribution of tags according to train set
                best_tag = self.weighted_random_by_dct()
                # if the word is unknown, current column filled by tags probabilities as they distribute on training set
                dynamic_table[:, i] = np.array([self.__tags_count_dict_normalized[tag] for tag in tags_lst])
            else:
                dynamic_table[:, i] = dynamic_table[:, i - 1] * \
                                     (self.__transition_df[tags_lst] @
                                      self.__emission_df.loc[tags_lst, cur_word])
                best_tag = tags_lst[int(np.argmax(dynamic_table[:, i]))]
            tags_MLE.append(best_tag)
        return tags_MLE

    def weighted_random_by_dct(self):
        rand_val = random.random()
        total = 0
        for k, v in self.__tags_count_dict_normalized.items():
            total += v
            if rand_val <= total:
                return k
        assert False, 'unreachable'

    def set_smoothing_coefficient(self, new_value):
        self.__smooth_coef = new_value
        self.__emission_df = self.get_emission_df()

    def get_transition_df(self):
        STOP = 'STOP'
        tags_set = self.__possible_tags.copy()
        tags_set.add(STOP)

        #  init DataFrame - table of transition probabilities, indexes - condition tag, column - conditioned tag
        transition_df = pd.DataFrame(0, dtype=np.float, index=self.__possible_tags, columns=self.__possible_tags)

        # init list of all tags sequences of length 2 presenting in the training sentences
        consecutive_tags = []
        for sentence in self.__train_set:
            tags_sequence = [sample[1] for sample in sentence] + [STOP]
            consecutive_tags += list(map(tuple, zip(tags_sequence, tags_sequence[1:])))

        #  init dictionary of all appeared tags sequences, mapped to their occurring frequencies
        samples_count_dict = Counter(consecutive_tags)

        #  filling the transition probabilities table
        for sample, count in samples_count_dict.items():
            transition_df.at[sample[0], sample[1]] = count

        # returning the DataFrame with each row (conditioning tag) being normalized
        # by its total quantity of appearances
        return transition_df.div(transition_df.sum(axis=1), axis=0)

    def get_emission_df(self):
        samples_count = Counter(self.__train_samples)

        #  init DataFrame - table of emission probabilities, indexes - condition tag, column - conditioned word
        emission_df = pd.DataFrame(0, dtype=np.float, index=self.__possible_tags, columns=self.__train_words)

        #  filling the transition probabilities table
        for sample, count in samples_count.items():  # emission_df.at[tag, word] = #(word, tag)
            emission_df.at[sample[1], sample[0]] = count + self.__smooth_coef

        return emission_df.div(emission_df.sum(axis=1), axis=0)
