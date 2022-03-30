import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(4, 4), index=["A", "B", "C", "D"], columns=["1", "2", "3", "4"])
# print(df)

# result_col= df[["1","2"]]      # Sütün yazdırımı
# print(result_col)

# result_row = df.loc["A"]    # Satır yazdırımı
# # loc["row", "column"] => loc["row"] => loc[:, "column"]
# print(result_row)

# result_col2 = df.loc[:, "1":"2"]  # =df.loc[:, ["1", "2"]]=result_col      # 1. ve 2. sütünu yazdırın, 2. de dahildir.
# print(result_col2) 

# result_both = result_col2 = df.loc["A":"C", "1":"2"] 
# print(result_both)

# result_iloc = df.iloc[1]     # İndex isimleri farklı olsa bile verilen sıradaki indeksi yazdırır.
# print(result_iloc)

# result_specValue = df.loc["B","3"]
# print(result_specValue)

# df["5"] = pd.Series(randn(4), ["A","B","C","D"])    # Sütun ekleme
# df["6"] = df["2"] + df["3"]
# print(df)

result_drop = df.drop("3", axis=1)   # Parantez içine inplace = True ifadesini eklersek orijinal df üzerinde de sütünu silebiliriz.
print(result_drop)