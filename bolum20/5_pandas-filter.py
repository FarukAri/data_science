from cgitb import reset
import pandas as pd
import numpy as np

data = np.random.randint(5, 100, 50).reshape(10, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df
# result = df.head(3)      # Baştan başlayarak içinde yazan sayı kadar satırı yazdırır.
# result = df.tail(4)      # Sondan başlayarak içinde yazan sayı kadar satırı yazdırır.
# result = df[["Column3","Column5"]].tail(4)      # Column 3-5 teki son 4 satır yazdırılır.
# result = df[5:15][["Column3","Column5"]].tail(4)      # Satırlar 5 ila 15 arasında indirgenir.

result = df > 50
result = df[df>50]
result = df[df["Column3"]>50]       # Column3 değerinin 50 den büyük olduğu satırları, satırdaki diğer değerlerle beraber getirir.
result = df[df["Column3"]>50]["Column3"]    # Sadece Column3 ün gelmesi için
result = df[(df["Column1"]<50) & (df["Column4"]>60)]   # "and" yerine "&" kullanılır.
result = df[(df["Column1"]<50) | (df["Column4"]>60)]    # "or" yerine "|" kullanılır.
result = df.query("Column1 >= 45 & Column3 %2 ==0")[["Column1","Column5"]]

print(df)
print(result)

