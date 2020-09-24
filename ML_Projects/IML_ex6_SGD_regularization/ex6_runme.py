import numpy as np
from load_data import get_digits
from SVM import *


def question19():
    batches = [5, 10, 25, 35, 40, 50, 60, 75, 85, 100]
    # batches = [5, 50, 100]
    iters = 150
    eta = 0.05
    X_train, y_train, X_test, y_test = get_digits(0, 1)
    y_train[y_train == 0] = -1
    y_test[y_test == 0] = -1
    initial_w = np.zeros(X_train.shape[1] + 1)
    for batch in batches:
        print("\n\nnum of batches = ", batch)
        w = sgd(X_train, y_train, iters, eta, initial_w, batch)
        # w = gd(X_train, y_train, iters, eta, initial_w)
        error = test_error(w, X_test, y_test)
        print(error)


if __name__ == '__main__':
    question19()
