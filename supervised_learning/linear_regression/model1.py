# import pandas as pd




#################### Train


import numpy as np
from matplotlib import pyplot as plt
plt.style.use('./deeplearning.mplstyle')


x_train = np.array([1,2])
y_train = np.array([300,500])

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# m is the number of training examples
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m}")


# # Plot the data points
# plt.scatter(x_train, y_train, marker='x', c='r')
# # Set the title
# plt.title("Housing Prices")
# # Set the y-axis label
# plt.ylabel('Price (in 1000s of dollars)')
# # Set the x-axis label
# plt.xlabel('Size (1000 sqft)')
# plt.show()


w = 100
b = 100

f_wb = np.zeros(m)
print(f_wb)
for i in range(m):
    f_wb[i] = w * x_train[i] + b 
    
print(f_wb)