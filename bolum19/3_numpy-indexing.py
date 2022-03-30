import numpy as np

numbers=np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[5]
result_2 = numbers[-1]
result_3 = numbers[:3]
result_4 = numbers[::-1]    # Listeyi ters çevirme
# print(result)

numbers_2 = np.array([[0, 1, 2, 20], [3, 4, 5, 50], [6, 7, 8, 80]])

result_2=numbers_2[1][0]    # = result_2=numbers_2[1,0]
result_3=numbers_2[:,1]
result_4=numbers_2[:2,1:3]
# print(result_2)
# print(result_3)
# print(result_4)

arr1 = np.arange(10)
# arr2 = arr1               # 2 dizi aynı kaynaktan veriyi çeker, o yüzden birinde yapılan değişiklik diğerini de etkiler. 
arr2 = arr1.copy()          # 2 farklı dizi oluşacağı için birinde yapılan değişiklik diğerini etkilemez.

arr2[1] = 11
print(arr1)
print(arr2)