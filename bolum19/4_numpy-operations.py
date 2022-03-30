import numpy as np

array1 = np.random.randint(5, 80, 15)
array2 = np.random.randint(5, 80, 15)

sumArray = array1 + array2
sumArray2 = array1 + 10

# print(sumArray)
# print(array1)
# print(sumArray2)

sinArray = np.sin(array1)
squareArray = np.sqrt(array1)
logArray = np.log(array1)

# print(sinArray)

multiArray1 = array1.reshape(3,5)
multiArray2 = array2.reshape(3,5)

# print(multiArray1)

verticalStackArray = np.vstack((multiArray1, multiArray2))      # Matrisleri dikey şekilde birleştirir.
horizontalStackArray = np.hstack((multiArray1, multiArray2))    # Matrisleri yatay şekilde birleştirir.

# print(verticalStackArray)
# print(horizontalStackArray)

isHigh = array1 >= 40

print(isHigh)
print(array1[isHigh])       # Sadece 40 dan büyük sayıları yazdırır.