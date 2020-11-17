import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def cleaning_data(train):
    #cleaning data :
    #1)unification of yr_buit and yr_renovated to single parameter.
    #2)drop of features that have low correlation with price and features that linearly dependent by some other features
    #3)drop all data with 3 standart deviation fat from mean
    #4)drop data with illigal price value (negative value)
    train["yr_built"] = train[["yr_built", "yr_renovated"]].max(axis=1,skipna=True)
    droped = train.drop(['date', "yr_renovated", "id", "long", "lat", "sqft_living"], axis=1)
    droped = droped[(np.abs(stats.zscore(droped)) < 3).all(axis=1)]
    droped=droped.ix[droped['price']>0]
    return droped

def find_corr_matrix(train):
    #return correlation matrix without date of salling and id.
    droped = train.drop(['id', 'date'], axis=1)
    return droped.corr()

def preprocessing(train):
    #spliting zipcode to dummy variables
    return train.join(pd.get_dummies(train['zipcode'])).drop(['zipcode'],axis=1)

def weight_calculating(train):
    #calculating of w according to formula w=(pseudoinverse transpose of X)*y
    y = train['price']
    X = train.drop(['price'], axis=1)
    w = np.dot(np.linalg.pinv(X), y)
    return w


def split_data(data, data_fraction):
    #split data to sample and train
    train = data.sample(frac=data_fraction)
    test = data.drop(train.index)
    return train, test


def loss_calculation(w, test):
    #calculatin of loss ERM
    y = test['price']
    X_transposed = test.drop(['price'], axis=1)
    loss = np.linalg.norm(X_transposed @ w - y) ** 2 / X_transposed.shape[0]
    return loss


def data_splitting_plot(data):
    train_loss = []
    test_loss=[]
    for i in range(1, 100):#% of train data to whole data
        train, test = split_data(data, i / 100)
        w = weight_calculating(train)
        train_loss.append(loss_calculation(w, train))
        test_loss.append(loss_calculation(w, test))
    plt.scatter(range(1, 100), (train_loss),label="train loss")
    plt.scatter(range(1, 100), (test_loss),label="test loss")
    plt.ylabel("loss")
    plt.xlabel("ratio of train data to all data in %")
    plt.title("linear regression with different training percents")
    plt.legend()
    plt.show()

def main():
    data = pd.read_csv("kc_house_data (1).csv").dropna()
    data = cleaning_data(data)
    corr = data.corr()
    data = preprocessing(data)
    xxt = data.transpose() @ data
    U,D,V =np.linalg.svd(xxt)
    data_splitting_plot(data)

if __name__ == '__main__':
    main()
