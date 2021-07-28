# Code to compute the clusters and labels

import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('./Data KO 14.csv') # data file with firing rates
y_true = pd.read_csv('./values.csv') # data file with actual labels
km = KMeans( n_clusters = 2).fit(df)
y_pred = km.labels_


# Code to compute the purity score

import numpy as np
from sklearn import metrics

def purity_score(y_true, y_pred):
    # compute contingency matrix (also called confusion matrix)
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    # return purity
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)

purity_score(y_true, y_pred)
