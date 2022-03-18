import numpy as np

height = [1.73 , 2.05 , 1.85, 1.94]
weight = [72.21, 93.31, 64.81, 88.21]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height**2

a = bmi>23
print(a)