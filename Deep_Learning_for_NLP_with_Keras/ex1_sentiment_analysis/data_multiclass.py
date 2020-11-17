from data import Data
from abc import abstractmethod
from keras.utils.np_utils import to_categorical

# TODO add heatmap plotting method
class DataMultiClass(Data):
    """
    Class for processing data for multiclass classification
    """
    @abstractmethod
    def vectorize_x(self):
        pass

    def vectorize_y(self):
        self.set_train_y(to_categorical(self.get_train_y(), dtype='float32'))
        self.set_test_y(to_categorical(self.get_test_y(), dtype='float32'))

    @abstractmethod
    def get_num_features(self):
        pass