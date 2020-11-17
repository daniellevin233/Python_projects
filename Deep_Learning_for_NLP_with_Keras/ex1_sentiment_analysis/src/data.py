from sklearn.model_selection import train_test_split
from abc import ABC, abstractmethod
import numpy as np

class Data(ABC):
    """
    Class for processing data for feeding it into neural networks
    """
    def __init__(self, x, y, test_ratio=0.1, val_ratio=0.0, k_fold=0, shuffle=True):
        if(test_ratio <= 0):
            print("Test set must be nonempty")
            exit()
        self.__train_x, self.__test_x, self.__train_y, self.__test_y  = \
            train_test_split(x, y, test_size=test_ratio, shuffle=shuffle)
        self.test_ratio = test_ratio
        self.val_ratio = val_ratio
        self.__k_fold = k_fold

    def train_val_split(self):
        """
        Split train set into smaller train set and validation set
        :return: 4-tuple (train_x, val_x, train_y, val_y)
        """
        # val ratio is relative to the entire data set, therefore it has to be adjusted to the size of the train data
        if(self.val_ratio <= 0):
            print("Validation set must be nonempty")
            exit()
        return train_test_split(self.__train_x, self.__train_y,
                                test_size=(self.val_ratio / (1. - self.test_ratio)),
                                shuffle=False)

    def is_k_fold_validation(self):
        return self.__k_fold > 0

    def get_num_of_folds(self):
        return self.__k_fold

    def train_val_split_gen(self):
        num_validation_samples = len(self.__train_x) // self.__k_fold
        for fold in range(self.__k_fold):
            training_x = self.__train_x[num_validation_samples * fold: num_validation_samples * (fold + 1)]
            validation_x = np.concatenate((self.__train_x[:num_validation_samples * fold],
                                            self.__train_x[num_validation_samples * (fold + 1):]))
            training_y = self.__train_y[num_validation_samples * fold: num_validation_samples * (fold + 1)]
            validation_y = np.concatenate((self.__train_y[:num_validation_samples * fold],
                                            self.__train_y[num_validation_samples * (fold + 1):]))
            yield (training_x, training_y, validation_x, validation_y)
        print("More k-fold validation circuits required than defined")
        exit()

    @abstractmethod
    def vectorize_x(self):
        pass

    @abstractmethod
    def vectorize_y(self):
        pass

    @abstractmethod
    def get_num_features(self):
        pass

    def get_train_x_y(self):
        return (self.__train_x, self.__train_y)

    def get_test_x_y(self):
        return (self.__train_x, self.__train_y)

    def get_train_x(self):
        return self.__train_x

    def set_train_x(self, x):
        self.__train_x = np.array(x)

    def get_train_y(self):
        return self.__train_y

    def set_train_y(self, y):
        self.__train_y = np.array(y)

    def get_test_x(self):
        return self.__test_x

    def set_test_x(self, x):
        self.__test_x = np.array(x)

    def get_test_y(self):
        return self.__test_y

    def set_test_y(self, y):
        self.__test_y = np.array(y)
