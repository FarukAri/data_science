import pandas as pd
import numpy as np

data = {
    "Column1" : [1, 2, 3, 4, 5],
    "Column2" : [15, 20, 25 , 30, 20],
    "Column3" : ["abec","adesd","bc","cba","dea"]
}

df = pd.DataFrame(data)
result = df
result = df["Column2"].unique()         # "Column2" deki ifadelerin tekrar etmeden listele
result = df["Column2"].nunique()        # Kaç farklı veri olduğunu söyler
result = df["Column2"].value_counts()   # Her bir elemandan kaç tane olduğunu yazdırır
result = df["Column1"] * 3              # Sayısal değerleri 3 ile çarpar

# def kullanarak istediğimiz fonksiyonu uygulama

def square(x) :
    return x*x

result = df["Column1"].apply(square) 

# lambda methodu ile istediğimiz fonksiyonu uygulama

square2 = lambda x: x*x

result = df["Column2"].apply(square2)  # =result = df["Column2"].apply( lambda x: x*x )

# Kolon uzunlukları

result = df["Column3"].apply(len)

# Kolondaki değerlerin uzunluğunu yeni kolona yazdırma

df["Length of Column3"] = df["Column3"].apply(len)

# print(df)

result = len(df.columns)        # Kolon sayısı
result = len(df.index)          # Satır sayısı

result = df.sort_values("Column2")      # Kolon2 yi numerik olarak sıralar, değişim tüm satırda olur.
result = df.sort_values("Column3")      # Kolon3 yi alfabetik olarak sıralar, değişim tüm satırda olur.
result = df.sort_values("Column2", ascending=False)     # Yüksekten düşüğe sıralama olur.
# print(result)

data = {
    "Ay" : ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs","Haziran","Nisan"],
    "Kategori" : ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir" : [20, 15, 53, 23,31,93,12,34,62]
}

df2 = pd.DataFrame(data)
result2 = df2.pivot_table(index= "Ay", columns="Kategori", values="Gelir")
print(result2)