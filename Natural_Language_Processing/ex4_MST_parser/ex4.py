import nltk
from nltk.corpus import dependency_treebank
from sklearn.model_selection import train_test_split
import numpy as np
from Chu_Liu_Edmonds_algorithm import *
from new_CLE_algorithm import *

ROOT_WORD = 'ROOT'
ROOT_TAG = 'TOP'


def get_vocabulary_and_tags(examples):
    words = set()
    tags = set()
    for graph in examples:
        for node in graph.nodes.values():
            if node['tag'] != ROOT_TAG:
                words.add(node['word'])
                tags.add(node['tag'])
    words.add(ROOT_WORD)
    tags.add(ROOT_TAG)
    return words, tags


def get_word_pair_idx(child, root, word_to_idx):
    child_idx = word_to_idx[child]
    root_idx = word_to_idx[root] if root is not None else word_to_idx[ROOT_WORD]
    return len(word_to_idx) * root_idx + child_idx


def get_tag_pair_idx(child, root, tag_to_idx, offset):
    child_idx = tag_to_idx[child]
    root_idx = tag_to_idx[root]
    return offset + len(tag_to_idx) * root_idx + child_idx


def get_graph_feature_vector(graph, arcs_lst, word_to_idx, tag_to_idx, in_features_len):
    graph_feature_vector = np.zeros(shape=(in_features_len, 1), dtype=int)
    for arc in arcs_lst:
        if graph.get_by_address(arc[0])['word'] in word_to_idx and graph.get_by_address(arc[2])['word']:
            graph_feature_vector[get_word_pair_idx(graph.get_by_address(arc[0])['word'],
                                                   graph.get_by_address(arc[2])['word'],
                                                   word_to_idx)] += 1
        if graph.get_by_address(arc[0])['tag'] in word_to_idx and graph.get_by_address(arc[2])['tag']:
            graph_feature_vector[get_tag_pair_idx(graph.get_by_address(arc[0])['tag'],
                                                  graph.get_by_address(arc[2])['tag'],
                                                  tag_to_idx, len(word_to_idx))] += 1
    return graph_feature_vector


def get_graph_distance_feature_vector(graph, arcs_lst, word_to_idx, tag_to_idx, in_features_len):
    graph_feature_vector = np.zeros(shape=(in_features_len, 1), dtype=int)
    for arc in arcs_lst:
        if graph.get_by_address(arc[0])['word'] in word_to_idx and graph.get_by_address(arc[2])['word']:
            graph_feature_vector[get_word_pair_idx(graph.get_by_address(arc[0])['word'],
                                                   graph.get_by_address(arc[2])['word'],
                                                   word_to_idx)] += 1
        if graph.get_by_address(arc[0])['tag'] in word_to_idx and graph.get_by_address(arc[2])['tag']:
            graph_feature_vector[get_tag_pair_idx(graph.get_by_address(arc[0])['tag'],
                                                  graph.get_by_address(arc[2])['tag'],
                                                  tag_to_idx, len(word_to_idx))] += 1
        distance = arc[2] - arc[0]
        if distance == 1:
            graph_feature_vector[-4] += 1
        else:
            word_distance = abs(arc[0] - arc[2])
            graph_feature_vector[-min(word_distance, 3)] += 1
    return graph_feature_vector


def arc_score(child, parent, theta, word_to_idx, tag_to_idx):
    if child['word'] in word_to_idx and parent['word'] in word_to_idx:
        return theta[get_word_pair_idx(child['word'], parent['word'], word_to_idx)] + \
               theta[get_tag_pair_idx(child['tag'], parent['tag'], tag_to_idx, len(word_to_idx))]
    else:
        return 0


def distance_arc_score(child, parent, theta, word_to_idx, tag_to_idx):
    distance = parent['address'] - child['address']
    if distance == 1:
        distance_idx = -4
    else:
        word_distance = abs(parent['address'] - child['address'])
        distance_idx = -min(word_distance, 3)
    if child['word'] in word_to_idx and parent['word'] in word_to_idx:
        return theta[get_word_pair_idx(child['word'], parent['word'], word_to_idx)] + \
               theta[get_tag_pair_idx(child['tag'], parent['tag'], tag_to_idx, len(word_to_idx))] + \
               theta[distance_idx]
    else:
        return 0


def get_graph_arc_lst(graph):
    arc_lst = []
    for tail in graph.nodes.values():
        for head_idx in tail['deps']['']:
            arc_lst.append(Arc(tail['address'], 0, graph.get_by_address(head_idx)['address']))
    return arc_lst


def get_complete_graph_arc_lst(graph, theta, word_to_idx, tag_to_idx, arc_score_func):
    arcs_lst = []
    for tail in graph.nodes.values():
        for head in graph.nodes.values():
            if tail['address'] != head['address'] and tail['tag'] != ROOT_TAG:
                arcs_lst.append(Arc(tail['address'], -arc_score_func(tail, head,
                                                               theta, word_to_idx, tag_to_idx), head['address']))
    return arcs_lst


def perceptron_train(n_iter, learn_rate, train_graphs, n_features, word_to_idx, tag_to_idx, feature_vector_func, arc_score_func):
    w = np.zeros(shape=(n_features, 1))
    w_sum = np.zeros(shape=(n_features, 1))
    for r in range(n_iter):
        # a = dict()
        # i = 0
        # start = datetime.datetime.now()
        for graph in train_graphs:
            # a[i] = (datetime.datetime.now() - start).total_seconds()
            # i += 1
            # if i % 10 == 0:
            #     print("Time wasted for 10 iterations: ", sum(a.values()) / 10)
            #     print()
            #     i = 0
            #     start = datetime.datetime.now()
            arc_lst = get_complete_graph_arc_lst(graph, w, word_to_idx, tag_to_idx, arc_score_func)
            learnt_arcs_dict = min_spanning_arborescence_nx(arc_lst, 0)
            w += learn_rate * (feature_vector_func(graph, get_graph_arc_lst(graph), word_to_idx, tag_to_idx, n_features) -
                               feature_vector_func(graph, learnt_arcs_dict.values(), word_to_idx, tag_to_idx, n_features))
            w_sum += w
    return w_sum / (n_iter * len(train_graphs))


def evaluate(w, test_set, word_to_idx, tag_to_idx, arc_score_func):
    sum = 0
    for graph in test_set:
        sum_per_sentence = 0
        arc_lst = get_complete_graph_arc_lst(graph, w, word_to_idx, tag_to_idx, arc_score_func)
        learnt_arcs_dict = min_spanning_arborescence_nx(arc_lst, 0)
        set_of_arcs = set([(arc[0], arc[2]) for arc in learnt_arcs_dict.values()])
        for tail in graph.nodes.values():
            for head_idx in tail['deps']['']:
                if (tail['address'], head_idx) in set_of_arcs:
                    sum_per_sentence += 1
        sum += sum_per_sentence / (len(graph.nodes) - 1)
    return sum / len(test_set)


if __name__ == '__main__':
    nltk.download('dependency_treebank')
    train_examples, test_examples = \
        train_test_split(dependency_treebank.parsed_sents(), train_size=0.9)

    vocabulary, tags = get_vocabulary_and_tags(train_examples)
    word_to_idx = {word: i for i, word in enumerate(vocabulary)}
    tag_to_idx = {tag: i for i, tag in enumerate(tags)}

    w1 = perceptron_train(2, 1, train_examples, len(vocabulary) ** 2 + len(tags) ** 2, word_to_idx, tag_to_idx, get_graph_feature_vector, arc_score)

    # with open('w1.pickle', 'wb') as f:
    #     pickle.dump(w1, f)
    # pickle_in = open("w1.pickle", "rb")
    # w1 = pickle.load(pickle_in)

    res = evaluate(w1, test_examples, word_to_idx, tag_to_idx, arc_score)
    print("Evaluate result: ", res)
    # if res > 0.17599643:
    #     with open('w1.pickle', 'wb') as f:
    #         pickle.dump(w1, f)

    w2 = perceptron_train(2, 1, train_examples, len(vocabulary) ** 2 + len(tags) ** 2 + 4, word_to_idx, tag_to_idx, get_graph_distance_feature_vector, distance_arc_score)
    res = evaluate(w2, test_examples, word_to_idx, tag_to_idx, distance_arc_score)
    print("Evaluate result with distance features ", res)
    # if res > 0.1012468:
    #     with open('w2.pickle', 'wb') as f:
    #         pickle.dump(w2, f)


