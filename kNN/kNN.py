# -*- coding: utf-8 -*-
"""kNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v5WxG6EnckcyQ8esEmPBDJ9cBSrzK_UM
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()

x=iris.data[:, [2,3]]
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1, stratify=y)

"""**Getting the dataset from** `sklearn`"""

iris = datasets.load_iris()

x=iris.data[:, [2,3]]
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1, stratify=y)

def plot_decision_regions(x,y, classifier,  test_idx = None, resolution = 0.02):
  from matplotlib.colors import ListedColormap

  # Marker generator + color map
  markers = ('s', 'x', 'o', '^', 'y')
  colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
  cmap = ListedColormap(colors[:len(np.unique(y))])
  
  # Plot decision surfaces
  x1_min, x1_max = x[:, 0].min() - 1, x[:, 0].max() + 1
  x2_min, x2_max = x[:, 1].min() - 1, x[:, 1].max() + 1
  xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                         np.arange(x2_min, x2_max, resolution))
  z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
  z = z.reshape(xx1.shape)
  plt.contourf(xx1, xx2, z, alpha = 0.3, cmap = cmap)
  plt.xlim(xx1.min(), xx1.max())
  plt.ylim(xx2.min(), xx2.max())
  # Plot examples
  for idx, cl in enumerate(np.unique(y)):
    c = "Iris Versicolor" if cl == 1 else "Iris Setosa"
    plt.scatter(x = x[y==cl, 0], y = x[y == cl, 1],
                alpha = 0.8,
                c = colors[idx],
                marker = markers[idx],
                label = c,
                edgecolor='black')
    if test_idx:
      x_test, y_test = x[test_idx, :], y[test_idx]
      plt.scatter(x_test[:, 0], x_test[:, 1], c ='', edgecolor='black', alpha = 1.0, linewidth=1, marker='o', s =100, label='test set')
  #plt.show()

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
x_combined_std = np.vstack((x_train_std, x_test_std))
y_combined = np.hstack((y_train, y_test))
x_combined = np.vstack((x_train, x_test))

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5, p = 2, metric = 'minkowski')
knn.fit(x_train_std, y_train)
plot_decision_regions(x_combined_std, y_combined, classifier=knn, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

