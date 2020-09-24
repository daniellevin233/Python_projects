import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import math


def norm_cdf(x, mean=0, var=1):
    return st.norm.cdf(x, loc=mean, scale=var)


def plot_cdf():
    t = np.arange(0.0, 10.0, 0.01)
    plt.title("Cumulative distribution function of Gaussians")
    axes = plt.gca()
    axes.set_xlabel("X")
    axes.set_ylabel("Φ(X | μ, σ^2)")
    axes.set_xlim([0, 10])
    plt.grid()
    plt.plot(t, norm_cdf(t, 4, 1), label="μ = 4, σ^2 = 1")
    plt.plot(t, norm_cdf(t, 6, 1), label="μ = 6, σ^2 = 1")
    plt.legend(loc='upper left')
    plt.show()


def norm_pdf(x, mean=0, var=1):
    return st.norm.pdf(x, loc=mean, scale=var)


def plot_pdf():
    t = np.arange(0.0, 10.0, 0.01)
    plt.title("Probability distribution function of Gaussians")
    axes = plt.gca()
    axes.set_xlabel("X")
    axes.set_ylabel("Φ(X | μ, σ^2)")
    axes.set_xlim([0, 10])
    plt.grid()
    plt.plot(t, norm_pdf(t, 4, 1), label="μ = 4, σ^2 = 1")
    plt.plot(t, norm_pdf(t, 6, 1), label="μ = 6, σ^2 = 1")
    plt.legend(loc='upper right')
    plt.show()


def logit(x):
    return np.log(x / (1 - x))


def inv_logit(x):
    return 1 / (1 + math.exp(-x))


def h(x, pi, mean=0, var=1):
    w = np.append(var, -0.5 * (mean ** 2) + math.log(pi))
    return [inv_logit(np.dot(np.append(y, 1), w)) for y in x]


def plot_h():
    t = np.arange(0.0, 30.0, 0.1)
    plt.title("Hypothesis function")
    axes = plt.gca()
    axes.set_xlabel("x")
    axes.set_ylabel("h(x)")
    axes.set_xlim([0, 30])
    plt.grid()
    plt.plot(t, h(t, 0.5, 4), label="μ = 4, σ^2 = 1, π = 0.5")
    plt.plot(t, h(t, 0.5, 6), label="μ = 6, σ^2 = 1, π = 0.5")
    plt.legend(loc='lower right')
    plt.show()


def normalize(arr):
    max, min = np.max(arr), np.min(arr)
    return [(val - min) / (max - min) for val in arr]


def get_cdf_values(x, pi, mean=0, var=1):
    return [(logit(val) + 0.5 * (mean ** 2) - math.log(pi)) / (var * 2) for val in x]


def plot_h_cdf(y):
    """
    x ~ X|(Y = y(0 or 1))
    """
    plt.title("Cumulative distribution function of h(x) for x ~ X|(Y = " + str(y) + ")")
    axes = plt.gca()
    axes.set_xlabel("x")
    axes.set_ylabel("cdf_h(x | X|(Y = " + str(y) + "))")
    axes.set_xlim([0, 1])
    plt.grid()
    mean = 4 if y == 0 else 6
    x_points = normalize(np.sort(np.random.normal(mean, 1, 1000)))
    plt.plot(x_points, norm_cdf(get_cdf_values(x_points, 0.5, mean), mean), label="μ = " + str(mean) + ", σ^2 = 1")
    plt.legend(loc='upper left')
    plt.show()


def plot_tpr_fpr():
    plt.title("TPR and FPR graph")
    axes = plt.gca()
    axes.set_xlabel("h(Z)")
    axes.set_ylabel("1 - CDF(h(Z))")
    axes.set_xlim([0, 1])
    plt.grid()
    mean_1, mean_2 = 4, 6
    z_1 = normalize(np.sort(np.random.normal(mean_1, 1, 1000)))
    z_2 = normalize(np.sort(np.random.normal(mean_2, 1, 1000)))
    plt.plot(h(z_1, 0.5, mean_1), 1 - norm_cdf(h(z_1, 0.5, mean_1), mean_1), label="μ = " + str(mean_1) + ", σ^2 = 1")
    plt.plot(h(z_2, 0.5, mean_2), 1 - norm_cdf(h(z_2, 0.5, mean_2), mean_2), label="μ = " + str(mean_2) + ", σ^2 = 1")
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    plot_h_cdf(0)
