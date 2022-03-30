import numpy as np

# 1- (10, 15, 30, 45, 60) dan oluşan numpy dizisi oluşturunuz.

# array1 = np.array([10, 15, 30, 45, 60])

# 2- (5-15) arasındaki sayılardan numpy dizisi oluşturunuz.

# array2 = np.arange(5,15)

# 3- (50-100) arasındaki sayılardan 5 er artmalı numpy dizisi oluşturunuz.

# array3 = np.arange(50,100,5)

# 4- 0 lardan oluşan 10 elemanlı bir numpy dizisi oluşturunuz.

# array4 = np.zeros(10)

# 5- 1 lerden oluşan 10 elemanlı bir numpy dizisi oluşturunuz.

# array5 = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

# array6 = np.linspace(0,100,5)
# print(array6)

# 7- (10-30) arasında rastgele 6 sayı üretin.

# array7 = np.random.randint(10, 30, 6)

# 8- -1 ile 1 arasında 30 sayı üretin.

# array8 = np.random.randn(30)
# print(array8)

# 9- 3x5 boyutlarında 10 ile 50 arasındaki sayılardan oluşan bir matris üretiniz.

multiarray1 = np.random.randint(-50, 50, 15).reshape(3, 5)
print(multiarray1)

# 10- Üretilen matrisin satır ve sütün sayılarını toplayınız.

# sumRow = multiarray1.sum(axis=1)
# sumColumn = multiarray1.sum(axis=0)
# print(sumRow)

# 11- Üretilen matrisin en büyük, en küçük ve ortalamasınız alınız.

# maxValue = multiarray1.max()
# minValue = multiarray1.min()
# avgArray = multiarray1.mean()
# print(maxValue)

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır?

# index_maxValue = multiarray1.argmax()
# print(index_maxValue)

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

# array = np.arange(10, 20)
# values = array[:3]

# 14- Üretilen dizinin elemanlarını tersten yazdırınız.

# reverseArray = array[::-1]

# 15- Üretilen multiArray1 matrisinin ilk satırını seçiniz.

# firstRow = multiarray1[0]
# print(firstRow)

# 16- Üretilen multiArray1 matrisinin 2. satır 3. sütundaki elemanı nedir?

# value1 = multiarray1[1,2]
# print(value1)

# 17- Üretilen multiArray1 matrisinin tüm satırlarındaki ilk elemanı seçiniz.

# array = multiarray1[:,0]
# print(array)

# 18- Üretilen multiArray1 matrisinin her bir elemanın karesini alınız

# squareArray = np.square(multiarray1)
# print(squareArray)

# 19- Üretilen multiArray1 matrisindeki hangi elemanlar pozitif çifit sayıdır? ( Aralığı -50, +50 arasında yapın)

evenNumber = multiarray1[multiarray1 %2 == 0]
posEvenNumber = evenNumber[evenNumber>0]
print(posEvenNumber)