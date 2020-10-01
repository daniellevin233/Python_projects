import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from preprocess import encode_hebrew, encode_russian, encode_korean
from sklearn.cluster import DBSCAN
from scipy.cluster.hierarchy import dendrogram, linkage, set_link_color_palette


def run_dbscan(X, ax):
    min_samples = np.arange(1, 11)
    num_of_clusters = []
    num_of_noises = []

    for min_sample in min_samples:
        db = DBSCAN(eps=0.8, min_samples=min_sample).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)

        num_of_clusters.append(n_clusters_)
        num_of_noises.append(n_noise_)

    ax.plot(min_samples, num_of_clusters, 'go-', label='Num of clusters', linewidth=2)
    ax.plot(min_samples, num_of_noises, 'rs-', label='Num of noise points', linewidth=2)
    ax.set(xlabel='Min samples')


def dbscan():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    run_dbscan(encode_hebrew().to_numpy(), ax1)
    ax1.set_title('DBSCAN for Hebrew verbs')
    run_dbscan(encode_russian()[1].to_numpy(), ax2)
    ax2.set_title('DBSCAN for Russian verbs')
    run_dbscan(encode_korean().to_numpy(), ax3)
    ax3.set_title('DBSCAN for Korean verbs')
    plt.legend()
    plt.show()

def plot_dendrogram(df, lang, color_threshold, method='complete'):
    linked = linkage(df, method=method, optimal_ordering=True)

    plt.figure(figsize=(10, 10))
    plt.title("{} dendrogram".format(lang))
    plt.xlabel("Distance")

    set_link_color_palette(['b', 'g', 'r', 'c', 'm', 'y'])

    dendrogram(linked,
               orientation='right',
               labels=df.index,
               distance_sort='ascending',
               color_threshold=color_threshold,
               above_threshold_color='k')

    plt.axvline(color_threshold, 0, 1, c='#ff8269ff', linestyle='dotted', linewidth=2)

    plt.show()


def plot_dendrogram_he():
    df = encode_hebrew().sample(frac=1)
    plot_dendrogram(df, 'Hebrew', 0.96)

def plot_dendrogram_ru():
    df_prefixes = encode_russian()[0].sample(frac=1)
    # plot_dendrogram(df_prefixes, 'Russian prefixes', 1.3)
    df = encode_russian()[1].sample(frac=1)
    plot_dendrogram(df, 'Russian', 1.3) # todo

def plot_dendrogram_kr():
    df = encode_korean().sample(frac=1)
    plot_dendrogram(df, 'Korean', 2.2, 'ward')

def plot_dendrogram_all():
    df_kr = encode_korean().sample(frac=1)
    df_ru = encode_russian()[1].sample(frac=1)
    df_he = encode_hebrew().sample(frac=1)
    df = pd.concat([df_he, df_ru, df_kr], axis=1, sort=False)
    plot_dendrogram(df, 'All the languages', 2.39)


if __name__ == '__main__':
    # dbscan()
    plot_dendrogram_he()
    # plot_dendrogram_ru()
    # plot_dendrogram_kr()
    # plot_dendrogram_all()