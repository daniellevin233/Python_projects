import numpy as np


def l_hinge(x, y, w):
    return np.max([0, 1 - y * np.dot(x, w)])


df = lambda x, y, w: -y * x if ((1 - y * np.dot(w, x)) > 0) else 0


def gd(data, label, iters, eta, w):
    """
    :param data: n x d numpy array, n - samples, d - dimension of each sample
    :param label: n x 1 numpy array, labels of each sample
    :param iters: integer, amount of iterations
    :param eta: a positive number defining the learning rate
    :param w: (d + 1) x 1 numpy array, d features and bias
    :return: (d + 1) x 1 numpy array, the output of the GD descent
                algorithm over ’iters’ iterations
    """
    ones = np.ones((data.shape[0], 1))
    data = np.concatenate((data, ones), axis=1)
    gradient = np.vectorize(df, excluded=['y', 'w'])
    s = np.zeros(shape=w.shape)
    for idx, next_x in enumerate(data):
        cur_w = w
        for i in range(iters):
            hinge_gradient = gradient(next_x, label[idx], cur_w)
            cur_w -= eta * hinge_gradient
        s += cur_w
    return s / data.shape[0]


def sgd(data, label, iters, eta, w, batch):
    """
    :param data: n x d numpy array, n - samples, d - dimension of each sample
    :param label: n x 1 numpy array, labels of each sample
    :param iters: integer, amount of iterations
    :param eta: a positive number defining the learning rate
    :param w: (d + 1) x 1 numpy array, d features and bias
    :param batch: the amount of samples that the algorithm would draw and use at each iteration
    :return: (d + 1) x 1 numpy array, the output of the GD descent
                algorithm over ’iters’ iterations
    """
    train = np.concatenate((data, label), axis=1)
    batch_idx = np.random.choice(np.arange(train.shape[0]), size=batch)
    return gd(train[batch_idx, :-1], train[batch_idx, -1], iters, eta, w)

def test_error(w, test_data, test_labels):
    """
    :param w: (d + 1) x 1 numpy array,
    :param test_data: n x d numpy array with n samples
    :param test_labels: n x 1 numpy array with the labels of the samples
    :return: a scalar with the respective 0-1 loss for the hypothesis
    """
    ones = np.ones(shape=(test_data.shape[0], 1))
    data = np.concatenate((test_data, ones), axis=1)
    return np.sum(np.abs(np.sign(np.dot(data, w)) - test_labels.T) / 2)
