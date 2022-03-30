import pandas as pd
import numpy as np

df = pd.read_csv("Players.csv")

# 1- İlk 10 kaydı getiriniz.

result = df.head(10)

# 2- Toplam kaç kayıt vardır?

result = len(df.index)

# 3- Tüm oyuncuların kiloları ortalaması kaçtır?

result = df['weight'].mean()

# 4- En kilolu oyuncu kaç kilodur?

result = df['weight'].max()

# 5- En kilolu oyuncu kimdir?

result = df[df['weight'] == df['weight'].max()]['Player'].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımı azalan şekilde ekrana getiriniz.

a = 2020 - df['born']

result =df[(20 <= a) & (a<= 25)][["Player","collage"]].sort_index(ascending= False)

# 7- "Kobe Bryant" isimli oyuncu nerede doğmuştur?

result = df[df["Player"] == "Kobe Bryant"][["Player", "birth_city"]]

# 8- "birth_state" lerine göre oyuncuların ortalama boyları

result = df.groupby("birth_state")["height"].mean()

# 9- Kaç farklı kolej mevcuttur?

result = df["collage"].nunique()

# 10- İsmi içinde "and" geçen oyuncuları bulunuz.

df = df.dropna()
result = df[df["Player"].str.contains("and")]

# def yöntemi ile

def str_findname(a):
    if "and" in a.lower():
        return True
    return False

result = df[df["Player"].apply(str_findname)]

print(result)