import numpy as np

# python list
pyt_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# numpy array
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(np_array))

np_multi = np_array.reshape(3, 3)
print(np_multi)

print(np_array.ndim)        # Dizinin boyutu hakkında bilgi verir.
print(np_multi.ndim)

print(np_array.shape)       # Dizinin ölçüleri hakkında bilgi verir.
print(np_multi.shape)