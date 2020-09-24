import numpy as np
from nltk.corpus import brown
from sklearn.model_selection import train_test_split
from Unigram import Unigram
from collections import Counter
from Bigram import Bigram
from Pseudowords import Pseudowords, Pseudoword


def simplify_complex_tags(tagged_sentences):
    """
    Complex tags from nltk corpus replaced by their prefix only: 'NN-JJ+DT' --> 'NN'
    :param tagged_sentences: list of tagged sentences from nltk corpus
    :param possible_tags: set containing all possible tags
    :type possible_tags: set
    :return: list of tagged sentences from nltk corpus with all the tags simplified
    """
    retagged_sentences = []
    for sentence in tagged_sentences:
        cur_sentence = []
        for sample in sentence:
            simplified_tag = sample[1].split('-')[0].split('+')[0]
            cur_sentence.append((sample[0], simplified_tag))
        retagged_sentences.append(cur_sentence)
    return retagged_sentences


def sentences_to_samples(train):
    """
    :param train: nd array of form: [sentence1, sentence2, ...] where:
    sentence1 = [('word1', 'tag1'), ('word1', 'tag1'), ]
    sentence2 = [('word3', 'tag3'), ('word4', 'tag1'), ]
    :return: np array containing all existing samples from the train with
             complex tags replaced by their prefixes ('NN-JJ+DT' --> 'NN')
    """
    new_train = []
    for sentence in train:
        for sample in sentence:
            new_train.append((sample[0], sample[1]))
    return np.array(new_train)


def unigram(train_sentences, test_sentences):
    #  processing of the sentences to tagged samples, since there's no importance to sentences structure
    train = sentences_to_samples(train_sentences)
    test = sentences_to_samples(test_sentences)

    unigram_HMM = Unigram(train)
    unigram_HMM.train()

    #  initialisation of lists of samples containing known and unknown words
    test_known_words, test_unknown_words = divide_test_to_known_and_unknown_samples(train_sentences, test_sentences)

    #  evaluation of the accuracy for each case
    print("Accuracy rate for unknown words: ", unigram_HMM.get_accuracy_rate(np.array(test_unknown_words)))
    print("Accuracy rate for known words: ", unigram_HMM.get_accuracy_rate(np.array(test_known_words)))
    print("Total accuracy rate: ", unigram_HMM.get_accuracy_rate(np.array(test)))


def divide_test_to_known_and_unknown_samples(train_sentences, test_sentences):
    test_known_words = list()
    test_unknown_words = list()

    samples = sentences_to_samples(train_sentences)
    train_words_set = set(sample[0] for sample in samples)

    for sentence in test_sentences:
        for sample in sentence:
            if isinstance(sample[0], Pseudoword) or sample[0] not in train_words_set:
                test_unknown_words.append(sample)
            else:
                test_known_words.append(sample)

    return test_known_words, test_unknown_words


def get_low_frequency_samples_lst(train_sentences):

    samples = sentences_to_samples(train_sentences)
    samples_count_dict = Counter(samples[:, 0])

    low_frequency_samples_lst = []
    frequent_samples_lst = []

    for sample, cnt in samples_count_dict.items():
        if cnt < 2:  # for pseudowords init purpose, creating set (not list) of samples is sufficient
            low_frequency_samples_lst.append(sample)  # repeating samples will be contained by this list only once
        else:
            frequent_samples_lst.append(sample)

    return low_frequency_samples_lst


def get_list_of_sentences_with_pseudowords(lst_of_sentences, words_to_pseudowords_dict):
    list_with_pseudowords = []
    for sentence in lst_of_sentences:
        sentence_with_pseudowords = []
        for sample in sentence:
            if sample[0] in words_to_pseudowords_dict:
                sentence_with_pseudowords.append((words_to_pseudowords_dict[sample[0]], sample[1]))
            else:
                sentence_with_pseudowords.append((sample[0], sample[1]))
        list_with_pseudowords.append(sentence_with_pseudowords)
    return list_with_pseudowords


def get_train_and_test_with_pseudowords(train_sentences_set, test_sentences_set):
    low_frequency_words = get_low_frequency_samples_lst(train_sentences_set)
    test_known_words, test_unknown_words = divide_test_to_known_and_unknown_samples(train_sentences_set,
                                                                                    test_sentences_set)
    # init class of pseudowords constructed of unknown words in test set and low-frequency words in the training set
    pseudowords = Pseudowords(low_frequency_words + test_unknown_words)
    words_to_pseudowords_dict = pseudowords.get_words_to_pseudowords_dict()

    # init sentences with pseudowords introduced
    train_with_pseudowords = get_list_of_sentences_with_pseudowords(train_sentences_set, words_to_pseudowords_dict)
    test_with_pseudowords = get_list_of_sentences_with_pseudowords(test_sentences_set, words_to_pseudowords_dict)

    return train_with_pseudowords, test_with_pseudowords


def main():
    #  importing tagged sentences
    tagged_sentences = brown.tagged_sents(categories=['news'])

    #  simplifying complex tags
    tagged_sentences = simplify_complex_tags(tagged_sentences)

    #  dividing to training and testing sets
    train, test = train_test_split(np.array(tagged_sentences), test_size=0.1, shuffle=False)

    # questions a, b
    print("Unigram HMM results: ")
    unigram(train, test)
    print()

    # question c
    bigram_HMM = Bigram(train)
    bigram_HMM.train()
    print("Bigram_HMM accuracy rate: ", bigram_HMM.get_accuracy_rate(np.array(test)))
    print()

    # question d - Add-one smoothing
    bigram_HMM.set_smoothing_coefficient(1)
    print("Bigram_HMM with add-one smoothing accuracy rate: ", bigram_HMM.get_accuracy_rate(np.array(test)))
    print()

    # question e(i, ii) - Pseudowords
    train_with_pseudo, test_with_pseudo = get_train_and_test_with_pseudowords(train, test)
    bigram_HMM_pseudowords = Bigram(train_with_pseudo)
    bigram_HMM_pseudowords.train()
    print("Bigram HMM with pseudowords accuracy rate: ", bigram_HMM_pseudowords.get_accuracy_rate(np.array(test_with_pseudo)))
    print()

    # question e(iii) - Pseudowords and add-one smoothing
    bigram_HMM_pseudowords.set_smoothing_coefficient(1)
    print("Bigram HMM with Add-one smoothing and pseudowords accuracy rate: ", bigram_HMM_pseudowords.get_accuracy_rate(np.array(test_with_pseudo)))
    print()

    print("Confusion matrix for bigram HMM with Add-one smoothing and pseudowords: ")
    print()
    confusion_matrix = bigram_HMM_pseudowords.get_confusion_matrix(test_with_pseudo)
    print(confusion_matrix)


if __name__ == '__main__':
    main()
