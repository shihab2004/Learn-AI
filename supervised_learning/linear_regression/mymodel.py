from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


train_data = pd.read_csv('datasets/train.csv')
# test_data = pd.read_csv('datasets/test.csv')



regr = LinearRegression()

X = train_data['x']
Y = train_data['y']


# regr.fit(X,Y)




# print(train_data['x'])
# plt.style.use('./deeplearning.mplstyle')
# plt.scatter(train_data['x'],train_data['y'], marker='x', c='r')
# plt.title('First Linier regression')
# plt.xlabel("Class No")
# plt.ylabel("Students")
# plt.show()


