from keras import layers
import numpy as np
from plot import plot_and_save

class NeuralNetwork:
    def __init__(self, data, model, activation_functions, nodes_by_layer, optimizer, loss, metrics,
                 dropout_rates=None, regularizers=None):
        """
        Parameters activation_functions, nodes_by_layer must be iterable of the same length
        dropout_rates, regularizers must be iterable shorter than activation_functions by one
        There is a preference of dropout over regularization if both are provided.
        :param data:
        :param model:
        :param activation_functions:
        :param nodes_by_layer:
        :param optimizer:
        :param loss:
        :param metrics:
        :param epochs:
        :param batch_size:
        :param dropout_rates:
        :param regularizers:
        """
        if regularizers is None:
            regularizers = []
        self.__data = data

        # network architecture parameters - NN structure dependent
        self.__model = model
        self.__activation_functions = activation_functions
        self.__nodes_by_layer = nodes_by_layer

        # compilation parameters - problem dependent
        self.__optimizer = optimizer
        self.__loss = loss
        self.__metrics = metrics

        # overfit overcoming parameters
        self.__dropout_rates = dropout_rates
        self.__regularizers = regularizers


    def build(self): # TODO customize layers - Dense --> general
        if(self.__dropout_rates): # apply dropouts to each layer
            self.build_with_dropout()
        elif(self.__regularizers): # add regularizers to each layer
            self.build_with_regularization()
        else: # neither dropout nor regularization were provided
            # input layer
            self.__model.add(layers.Dense(self.__nodes_by_layer[0],
                             activation=self.__activation_functions[0],
                             input_shape=(self.__data.get_num_features(),)))

            # remaining - intermediate and output layers
            for i_layer in range(1, len(self.__activation_functions)):
                self.__model.add(layers.Dense(self.__nodes_by_layer[i_layer],
                                              activation=self.__activation_functions[i_layer]))

            # compile the model
            self.__model.compile(optimizer=self.__optimizer,
                                 loss=self.__loss,
                                 metrics=self.__metrics)

    def build_with_dropout(self):
        # input layer
        self.__model.add(layers.Dense(self.__nodes_by_layer[0],
                         activation=self.__activation_functions[0],
                         input_shape=(self.__data.get_num_features(),)))
        self.__model.add(layers.Dropout(self.__dropout_rates[0]))

        # intermediate layers
        for i_layer in range(1, len(self.__activation_functions) - 1):
            self.__model.add(layers.Dense(self.__nodes_by_layer[i_layer],
                                          activation=self.__activation_functions[i_layer]))
            self.__model.add(layers.Dropout(self.__dropout_rates[i_layer]))

        # output layer
        self.__model.add(layers.Dense(self.__nodes_by_layer[-1],
                         activation=self.__activation_functions[-1]))

        # compile the model
        self.__model.compile(optimizer=self.__optimizer,
                             loss=self.__loss,
                             metrics=self.__metrics)

    def build_with_regularization(self):
        # input layer
        self.__model.add(layers.Dense(self.__nodes_by_layer[0],
                         activation=self.__activation_functions[0],
                         input_shape=(self.__data.get_num_features(),),
                         kernel_regularizer=self.__regularizers[0]))

        # intermediate layers
        for i_layer in range(1, len(self.__activation_functions) - 1):
            self.__model.add(layers.Dense(self.__nodes_by_layer[i_layer],
                                          activation=self.__activation_functions[i_layer],
                                          kernel_regularizer=self.__regularizers[i_layer]))

        # output layer
        self.__model.add(layers.Dense(self.__nodes_by_layer[-1],
                                      activation=self.__activation_functions[-1]))

        # compile the model
        self.__model.compile(optimizer=self.__optimizer,
                             loss=self.__loss,
                             metrics=self.__metrics)

    def fit_k_fold(self, epochs, batch_size):
        validation_scores = []
        split_gen = self.__data.train_val_split_gen()
        for fold in range(self.__data.get_num_of_folds()):
            x_train, y_train, x_val, y_val = next(split_gen)
            self.__model.fit(x_train,
                             y_train,
                             epochs=epochs,
                             batch_size=batch_size)
            validation_score = self.__model.evaluate(x_val, y_val,
                                                     batch_size=batch_size)
            validation_scores.append(validation_score)
        self.validation_score = np.average(validation_scores, axis=0)

    def fit(self, epochs=10, batch_size=128):
        if(self.__data.is_k_fold_validation()):
            self.fit_k_fold(epochs, batch_size)
        else:
            partial_x_train, x_val, partial_y_train, y_val = \
                self.__data.train_val_split()

            self.history = self.__model.fit(partial_x_train,
                                            partial_y_train,
                                            epochs=epochs,
                                            batch_size=batch_size,
                                            validation_data=(x_val, y_val))

    def evaluate(self, batch_size=128):
        res = self.__model.evaluate(self.__data.get_test_x(),
                                    self.__data.get_test_y(),
                                    batch_size=batch_size)
        print("test loss, test acc: ", res)
        return res

    def get_loss_history(self):
        return [self.history.history['loss'], self.history.history['val_loss']]

    def get_accuracy_history(self):
        return [self.history.history['accuracy'], self.history.history['val_accuracy']]

    def predict(self, x_test):
        self.__model.predict(x_test)

    def tune_epochs(self, epochs, path):
        """

        :param epochs: num of epochs
        :param path:
        :return:
        """

        self.fit(epochs=epochs, batch_size=256)

        loss = self.history.history['loss']
        val_loss = self.history.history['val_loss']

        accuracy = self.history.history['accuracy']
        val_accuracy = self.history.history['val_accuracy']

        plot_and_save(range(1, len(loss) + 1), [loss, val_loss], path.format('epochs_loss'),
                      labels=['Training loss', 'Validation loss'], title='Training and validation loss to epochs',
                      x_label='Epochs', y_label='Loss')

        plot_and_save(range(1, len(loss) + 1), [accuracy, val_accuracy], path.format('epochs_accuracy'),
                      labels=['Training accuracy', 'Validation accuracy'], title='Training and validation accuracy to epochs',
                      x_label='Epochs', y_label='Accuracy', ylim=(0.2, 1))


