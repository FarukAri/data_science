import pandas as pd 
import numpy as np

personeller = {
    "Çalışan" : ["Ahmet Yılmaz", "Can Ertürk", "Hasan Korkmaz", "Cenk Saymaz", "Ali Turan", "Rıza Ertürk", "Mustafa Can"],
    "Departman": ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
    "Yaş" : [30, 25, 45, 50, 23, 34, 42],
    "Semt" : ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Kadıköy", "Tuzla", "Maltepe"],
    "Maaş" : [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df = pd.DataFrame(personeller, index= [1, 2, 3, 4, 5, 6, 7])
result = df

# result = df["Maaş"].sum()       # Maaşların toplamı
# result =df.groupby("Departman").groups
# result =df.groupby(["Departman", "Semt"]).groups


# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)

# result =  df.groupby("Departman").get_group("Muhasebe")         # Sadece muhasebe departmanında çalışanların yazdırılması için
# result =  df.groupby("Departman").sum()                         # Departmanlardaki sayısal verilerin toplamı için
# result =  df.groupby("Semt").mean()                             # Ortalama
# result =  df.groupby("Departman")["Maaş"].max()                 # Departmanlardaki max maaş miktarları
# result =  df.groupby("Semt")["Maaş"].mean()
# result =  df.groupby("Semt").get_group("Tuzla")["Yaş"].min()   # Tuzla'daki minimum yaş
# result =  df.groupby("Semt")["Maaş"].mean()["Kadıköy"]         # Kadıköy'deki ortalama maaş

result = df.groupby("Departman")[["Maaş", "Yaş"]].agg([np.mean, np.sum, np.max])       # Numpy methodları ile uygulama


print(result)
