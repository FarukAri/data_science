import numpy as np

# result = np.arange(1, 10)               # 1 den 10 a kadar sıralı dizi, 10 dahil değil.
# result_2 = np.arange(10, 100, 5)        # 10 dan 100 e kadar dizi oluşturur, artış miktarı 5 dir.
# print(result, result_2)

# result_3 = np.zeros(10)                 # 10 tane 0 dan oluşan dizi oluşturur.
# result_4 = np.ones(10)                  # 10 tane 1 den oluşan dizi oluşturur.
# print(result_3, result_4)

# result_5 = np.linspace(0, 100, 8)            # 0 ile 100 arasında eşit 8 parçadan oluşan dizi oluşturur. 
# print(result_5)

# result_6 = np.random.randint(10)             # 0 ile 10 arasında (10 dahil değil) rastgele 1 integer seçer.
# result_7 = np.random.randint(2, 10, 4)       # 2 ile 10 arasında rastgele 4 integerdan bir dizi oluşturur.
# print(result_6, result_7)
# print(type(result_7))

# result_8 = np.random.rand(4)            # 0 ile 1 arasında rastgel 4 tane sayıdan oluşan dizi oluşturur.
# result_9 = np.random.randn(4)           # -1 ile 1 arasında
# print(result_8, result_9)

# np_array = np.arange(40)
# np_multi = np_array.reshape(4, 10)
# print(np_multi)
# print(np_multi.shape)
# print(np_multi.sum(axis=1))     # Satırların toplamı
# print(np_multi.sum(axis=0))     # Sütünların toplamı

rnd_numbers = np.random.randint(0, 80, 15)
print(rnd_numbers)
print(rnd_numbers.max())            # Üretilen en büyük sayı. min ile de en küçüğü bulunur.
print(rnd_numbers.mean())
print(rnd_numbers.argmax())         # Üretilen en büyük sayının index numarasını verir.
