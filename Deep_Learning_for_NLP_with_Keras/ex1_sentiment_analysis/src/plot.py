from matplotlib import pyplot as plt

DEF_COLORS_DOTS = ['or',
                   'og',
                   'ob',
                   'oc',
                   'om',
                   'oy',
                   'ok',
                   'ow']

DEF_COLORS_LINE = ['r',
                   'g',
                   'b',
                   'c',
                   'm',
                   'y',
                   'k',
                   'w' ]

def plot_and_save(x, y, path, labels, title, x_label, y_label, xlim=None, ylim=None, show=False):
    """
    Plots scatters plots for single x axis and several functions as provided by y
    :param x: definition field of the function
    :param y: must be list of lists - each represents a separate function
    :param path: relative path to save the plot
    :param labels: list of labels for legend
    :param titles: list of titles
    """
    plt.clf()
    for plt_i in range(len(y)):
        plt.plot(x, y[plt_i], DEF_COLORS_DOTS[plt_i], label=labels[plt_i])

    plt.xlabel(x_label)
    plt.xticks(x)
    if(xlim):
        plt.xlim(xlim[0], xlim[1])
    plt.ylabel(y_label)
    if (ylim):
        plt.ylim(ylim[0], ylim[1])
    plt.title(title)
    plt.legend()
    plt.savefig(path)
    if(show):
        plt.show()

