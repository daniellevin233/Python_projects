##############################################################################
# FILE : ex9.py
# WRITER : Daniel Levin , daniellevin , 336462874
# EXERCISE : intro2cs ex8 2017-2018
# DESCRIPTION: Building the binary decision trees
# for defining the best diagnoses
# Realisation of different function for working with trees inside Diagnoser
# class
# Classes: Node, Record, Diagnoser
##############################################################################

###########
# imports #
###########

from itertools import combinations

#############
# constants #
#############

REC_ILLNESS = 0  # the position in which a record entry is split into key
REC_SYMPTS = 1  # and values.
ROOT_DEPTH = 0


######################
# Classes definition #
######################

class Node:
    def __init__(self, data="", pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """
    Reads a records text file, splits every record line into "illness" and
    "symptoms"
    returns a list of record objects constructed from those values.
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.split()
            records.append(Record(words[REC_ILLNESS], words[REC_SYMPTS:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.__root = root

    def diagnose(self, symptoms):
        """
        Method fix the diagnose in accordance to symptoms, using the binary
        decision tree
        :param symptoms:list of strings - symptoms that we use to fix illness
        :return: string - illness that was got as outcome of symptoms
        """
        cur_root = self.__root
        illness = self.diagnose_helper(symptoms, cur_root)
        return illness

    def diagnose_helper(self, symptoms, tree_root):
        """
        Helper method that uses recursion to come down on the binary tree
        and fix the proper illness
        :param symptoms:list of strings - symptoms that we use to fix illness
        :param tree_root: object of type Node - current root of the tree (subtree)
        check its data if it is one of given symptoms or not. In this way
        happens fixing if answer - 'Yes' or 'No'
        :return: string - illness
        """
        if not tree_root.positive_child:  # the base case - we are on the leaf
            illness = tree_root.data
            return illness
        if tree_root.data in symptoms:  # the answer is 'Yes'
            tree_root = tree_root.positive_child
        else:
            tree_root = tree_root.negative_child  # the answer is 'No'
        return self.diagnose_helper(symptoms, tree_root)

    def calculate_error_rate(self, records):
        """
        This method counts the rate of errors for fixing diagnose in the
        relation to real illness. (The rate of errors that method diagnose
        makes.
        :param records: list of objects of type Record that contains
        symptoms list and real illness
        :return: float - rate of errors
        """
        errors = 0
        for cur_record in records:
            hypo_illness = self.diagnose(cur_record.symptoms)
            if hypo_illness != cur_record.illness:
                errors += 1
        return errors / len(records)

    def all_illnesses(self):
        """
        This method finds all illnesses that appear in the tree - in other
        words all leafs of the tree
        :return: list of strings - illnesses
        """
        tree_root = self.__root
        all_illnesses_lst = self.all_illnesses_helper(tree_root)
        return all_illnesses_lst

    def all_illnesses_helper(self, tree_root, illnesses_set=set()):
        """
        This method is recursive search of leafs of tree with a root cur_root.
        :param tree_root: the object of type Node - root that we are staring
        from
        :param illnesses_set: set of illnesses we will add the strings to
        it is comfortable to use set hence it gives opportunity not to add
        the same illnesses several times.
        :return:lexicographic sorted list of illnesses
        """
        if not tree_root.positive_child:  # the base case - we are on the leaf
            return illnesses_set.add(tree_root.data)
        self.all_illnesses_helper(tree_root.positive_child)
        self.all_illnesses_helper(tree_root.negative_child)
        return sorted(illnesses_set)  # function sorted()
        # return a new sorted list from elements in the set

    def most_common_illness(self, records):
        """
        Method define the most common illness out of all diagnoses.
        Implement the dictionary with illnesses as keys, and starting
        values 0 for each illness - (1)
        Increasing the value of illness by 1 if it was diagnosed - (2)
        Fixing the biggest index out of values of the dictionary - (3)
        :param records: list of objects of type Record that contains
        symptoms list and real illness
        :return:string - the most common diagnosed illness
        """
        illnesses_dict = dict.fromkeys(self.all_illnesses(), 0)  # (1)
        for cur_record in records:
            hypo_illness = self.diagnose(cur_record.symptoms)
            illnesses_dict[hypo_illness] += 1  # (2)
        illness = max(illnesses_dict, key=illnesses_dict.get)  # (3)
        return illness

    def paths_to_illness(self, illness):
        """
        Method creates list of paths by calling to recursive helper function
        :param illness: string - the desired illness
        :return: list of lists containing series of True and False -
        representing the path from tree root to leaf in binary decision tree
        """
        tree_root = self.__root
        paths = self.paths_to_illness_helper(tree_root, illness)
        return paths

    def paths_to_illness_helper(self, tree_root, illness, paths_lst=[],
                                current_path=[]):
        """
        Recursive method that creates list of lists that contain boolean
        representation of paths from tree_root to illness in binary tree
        :param tree_root: object of type Node - root of the tree
        :param illness: string - illness that we are looking pathes to
        :param paths_lst: the entire list of pathes that we will implement
        during the recursion
        :param current_path: list representing each path from root to leafs
        :return: list of paths - from root to desired illness
        """
        if not tree_root.positive_child:  # the base case - we are on the leaf
            if tree_root.data == illness:  # we got the desired illness
                paths_lst.append(current_path)
            return
        self.paths_to_illness_helper(tree_root.positive_child, illness,
                                     paths_lst, current_path + [True])
        self.paths_to_illness_helper(tree_root.negative_child, illness,
                                     paths_lst, current_path + [False])
        return paths_lst


def build_tree(records, symptoms):
    """
    Function that builds the binary decision complete tree.
    By calling to recursive function build_tree_helper
    :param records: list of objects of type Record that contains
    symptoms list and real illness
    :param symptoms: list of strings - symptoms - on each level in the tree
    will be the same symptom.
    :return: object of type Node - the root of the tree
    """
    depth = ROOT_DEPTH
    tree_root = Node(symptoms[ROOT_DEPTH])  # declare the root
    depth += 1
    build_tree_helper(tree_root, records, symptoms, depth)
    return tree_root


def build_tree_helper(root, records, symptoms, cur_depth,
                      yes_symptoms_lst=[], no_symptoms_lst=[]):
    """
    The recursive helper function that builds binary complete tree.
    Leafs - illnesses, all the other nodes - symptoms.
    :param root: object of type Node - the root of the tree
    :param records: list of objects of type Record that contains
    symptoms list and real illness
    :param symptoms: list of strings - symptoms - on each level in the tree
    will be the same symptom. So tree height = len(symptoms)
    :param cur_depth: integer that denotes the current depth of the tree
    :param yes_symptoms_lst: list of symptoms containing only symptoms that
    their answer was "yes" - implementing the list during the recursion
    :return: -
    """
    if cur_depth == len(symptoms):  # the basic case - we are before leafs
        pos_illness = fix_illness_for_leaf(yes_symptoms_lst + [symptoms[-1]],
                                           no_symptoms_lst, records)
        # for last positive answer need to add the last symptom to yes_list
        neg_illness = fix_illness_for_leaf(yes_symptoms_lst, no_symptoms_lst +
                                           [symptoms[-1]], records)
        # the last answer is "No" - add the last symptom to no_list
        root.positive_child = Node(pos_illness)
        root.negative_child = Node(neg_illness)
        # putting the proper illnesses to leafs
        return
    cur_symptom = symptoms[cur_depth]
    pos_child = root.positive_child = Node(cur_symptom)  # denote node
    neg_child = root.negative_child = Node(cur_symptom)  # denote node
    build_tree_helper(pos_child, records, symptoms, cur_depth + 1,
                      yes_symptoms_lst + [symptoms[cur_depth - 1]],
                      no_symptoms_lst)
    # need to add previous symptom ("Yes"), and increase cur_depth
    build_tree_helper(neg_child, records, symptoms, cur_depth + 1,
                      yes_symptoms_lst, no_symptoms_lst +
                      [symptoms[cur_depth - 1]])
    # need to add previous symptom ("No"), and increase cur_depth
    # recursive calls for right and left subtrees
    # in the case of left subtree (positive answer - "Yes")
    # add to yes_symptoms_list current symptom (answer was "yes")
    return


def fix_illness_for_leaf(yes_symptoms_lst, no_symptoms_lst, records):
    """
    Function fix the illness appearing most frequently in the records
    illnesses by comparing it symptoms list with the given parameter
    symptoms_lst. The sets are used to think over change in symptoms
    order. Firstly the dictionary is created with illnesses from records
    as keys and 0 as values.
    Then if list of symptoms do NOT contain any symptom of no_symptoms_lst (1)
    and contains all the symptoms of the yes_symptoms_lst (2),
    then increasing counter of current illness by 1.
    Finally searching the maximal counter between the values of dictionary
    and returning corresponding illness.
    :param yes_symptoms_lst: list of symptoms from tree that got the answer "Yes"
    :param no_symptoms_lst: list of symptoms from tree that got the answer "No"
    :param records: list of objects of type Record - pairs :
    illness - symptoms_lst.
    :return:string - the most frequent illness of the records that satisfy
    given symptoms.
    """
    illnesses_dict = {rec.illness: 0 for rec in records}
    # denote the dict with illnesses as keys, their frequency as values
    for record in records:
        need_to_add_this_illness = True
        for no_symptom in no_symptoms_lst:
            if no_symptom in record.symptoms:  # (1)
                need_to_add_this_illness = False
        if not set(yes_symptoms_lst).issubset(set(record.symptoms)):  # (2)
            need_to_add_this_illness = False
        if need_to_add_this_illness:
            illnesses_dict[record.illness] += 1
    illness = max(illnesses_dict, key=illnesses_dict.get)
    return illness


def optimal_tree(records, symptoms, depth):
    """
    This function builds the optimal tree: the tree with minimal error
    rate for diagnosing the illness in accordance to given records and
    symptoms. The tree will be by height - depth + 1.
    :param records:list of objects of type Record - pairs :
    illness - symptoms_lst.
    :param symptoms: list of strings - symptoms from which will be constructed
    combinations for building tree and the asking questions correspondingly.
    :param depth: the size of combination of symptoms that will be constructed
    for building the tree and consequently the height of the tree - 1
    :return: object of type Node - root of the optimal tree
    """
    min_error_rate = 1  # the maximal possible error rate is 1 (100%)
    tree_root_dict = {}  # the dictionary that will be implemented
    # during the function: keys - tree roots, values - error rate of the tree
    all_combination = combinations(symptoms, depth)  # proper combinations
    for cur_combination in all_combination:
        cur_root = build_tree(records, list(cur_combination))  # build curtree
        cur_diagnoser = Diagnoser(cur_root)  # initialize Diagnoser object
        cur_error_rate = cur_diagnoser.calculate_error_rate(records)
        # counting the error rate for current tree
        if cur_error_rate <= min_error_rate:  # this condition is to safe
            # running time and not to add every root to dictionary keys
            min_error_rate = cur_error_rate
            # updating the minimal error rate value
            tree_root_dict.update({cur_root: cur_error_rate})
            # update the tree_roots - error_rates dictionary
    optimal_tree_root = min(tree_root_dict, key=tree_root_dict.get)
    return optimal_tree_root


if __name__ == "__main__":
    """Tests for implemented functions"""

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    # build leaves
    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    healthy_leaf = Node("healthy", None, None)

    # connect two leaves to new inner vertex
    inner_vertex = Node("fever", flu_leaf, cold_leaf)

    # connect inner vertex and another leaf into new root node
    root = Node("cough", inner_vertex, healthy_leaf)

    # create diagnoser object initialized with the root we just created
    diagnoser = Diagnoser(root)
    #################
    # Simple test 1 #
    #################
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test 1 passed")
    else:
        print("Test 1 failed. Should have printed cold, printed: ", diagnosis)
    #################
    # Simple test 2 #
    #################
    record1 = Record("influenza", ["cough", "fever"])
    record2 = Record("cold", ["cough"])
    record3 = Record("healthy", [])
    records = [record1, record2, record3]
    if diagnoser.calculate_error_rate(records) == 0:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
    #################
    # Simple test 3 #
    #################
    if diagnoser.all_illnesses() == ['cold', 'healthy', 'influenza']:
        print("Test 3 passed")
    else:
        print("Test 3 failed")
    #################
    # Simple test 4 #
    #################
    rec1 = Record("influenza", ["cough", "fever"])
    rec2 = Record("cold", ["cough"])
    rec3 = Record("healthy", ['cough'])
    records = [rec1, rec2, rec3]
    if diagnoser.most_common_illness(records) == 'cold':
        print("Test 4 passed")
    else:
        print("Test 4 failed")
    #################
    # Simple test 5 #
    #################
    if diagnoser.paths_to_illness('healthy') == [[False]]:
        print("Test 5 passed")
    else:
        print("Test 5 failed")
