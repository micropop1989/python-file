#cmd
#cd C:\Users\lcg\AppData\Local\Programs\Python\Python38-32\Scripts
#pip  install numpy

import numpy as np
from numpy import random  #one of function of numpy

arr = np.array([1, 2, 5, 6])
arr1 = np.array([1, 2, 3, 4],ndmin=5)
arr2 = np.array([[1, 2, 5, 6], [4, 6, 7, 8]])

print(np.__version__)
print(arr)


print(arr1)
print('shape of array :', arr1.shape)
print(arr2.shape)

print(random.randint(90)) #print ramdom number 0-90
print(random.randint(90, size=(3, 5))) #print ramdom array  3rows, 5 elements each row
print(random.rand()) #print ramdom float number
print(random.randint(90, size=(5))) #print ramdom 1d array with 5 elements
print(random.choice([3, 29, 6, 9, 10, 39])) #print ramdom number from array
print(random.choice([3, 29, 6, 9, 10, 39], p=[0.1, 0.2, 0.2, 0.05, 0.25, 0.2], size=(100))) #print array with 100 elements by probability q
print(random.choice([3, 29, 6, 9, 10, 39], p=[0.1, 0.2, 0.2, 0.05, 0.25, 0.2], size=(4, 10))) #print array with 100 elements by probability q



