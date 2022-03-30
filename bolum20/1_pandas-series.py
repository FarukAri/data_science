import pandas as pd

numbers =[10, 20 ,30 ,40]
letters = ["a", "b", "c"]
dict = {'a':10, 'b':20, 'c':30}

# pandas_series = pd.Series(numbers)
# pandas_series2 = pd.Series(letters)
# pandas_series4 = pd.Series(dict)
pandas_series3 = pd.Series(numbers, ['birinci', 'ikinci', 'üçüncü', 'dördüncü'])

# print(pandas_series)
# print(pandas_series2)
# print(pandas_series3)
# print(pandas_series3[-1])
# print(pandas_series3[:2])
# print(pandas_series3['birinci'])
# print(pandas_series4)

# result = pandas_series3[['birinci','ikinci']]
# result = pandas_series3.ndim                      # Dimension bilgisi için (Boyut bilgisi)
# result = pandas_series3.shape                     # Ölçüleri için
# result = pandas_series3.dtype                     # Tipi için
# result = pandas_series3.sum()
# result = pandas_series3.max()
# result = pandas_series3.min()
# result = pandas_series3 + pandas_series3          # Değerleri toplar
# result = pandas_series3 >=50                      # Diğer matematik operatörlerini de kullanabiliriz
# result = pandas_series3 %8 == 0

# print(result)
# print(pandas_series3[result])

fiat2018 = pd.Series([20, 30, 40, 10], ['Punto', 'Linea', 'Egea', 'Fiorino'])
fiat2019 = pd.Series([15, 20, 45, 30], ['Punto', 'Linea', 'Egea', '500L'])

total = fiat2018 + fiat2019
print(total)
print(total['Punto'])
