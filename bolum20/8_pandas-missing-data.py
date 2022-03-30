import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)
df = pd.DataFrame(data, index=["a", "c", "e","f","h"], columns = ["column1", "column2", "column3"])

df = df.reindex(["a", "b", "c", "d", "e", "f", "g","h"])

# result = df.drop("column1", axis=1)         # Column silme
# result = df.drop(["a", "f"], axis=0)        # Row silme
# result = df.isnull()                        # NaN sorgusu (NaN ise True verir)
# result = df.notnull()                       # isnull un tam tersi

newColumn = [18, np.nan, 73, np.nan, 88, np.nan, 23, np.nan]
df["column4"] = newColumn

# result = df[df["column2"].isnull()]         # Sadece 2. kolonun NaN olduğu dizileri gösterir
# result = df[df["column3"].notnull()]["column3"]       

# result = df.dropna()                        # Default hali axis=0 olduğu için NaN içeren satırları siler
# result = df.dropna(axis=1)                  # NaN içeren sütunları temizler
# result = df.dropna(how = "all")             # Sadece bütün değerleri NaN olan satırları siler
# result = df.dropna( subset = ["column1", "column3"], how = "all")   #  1. ve 3. kolonlara özel arama yapar
# result = df.dropna( thresh = 2 )            # Satırda iki tane gerçek değer varsa silmez.

# result = df.fillna( value = "No Info")      # NaN olan yerlere istenilen şeyi yazar. 

# result = df.fillna( value = 1)

def ortalama(df):
    toplam = df.sum().sum()            # Tek sum kolonların toplamını 2 sum bütün değerlerin toplamını yazar
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna( value = ortalama(df))


print(result)