from unittest import result
import pandas as pd

df = pd.read_csv("datasets/imdb.csv")
# print(df)

# 1- İlk 5 kaydı göster

# result = df.head(5)

# 2- Son 10 kaydı göster

# result = df.tail(10)

# 3- Sadece "title" kolonunu seçin

# result = df["title"]

# 4- Sadece "title" kolonunu içeren ilk 5 kaydı alın

# result = df["title"].head(5)

# 5- "title" ve "imdbrating" kolonunu içeren son 7 kaydı alın

# result = df[["title", "imdbrating"]].tail(7)

# 6- "title" ve "imdbrating" kolonunu içeren 2. 5 kaydı alın

# result = df[5:15][["title", "imdbrating"]].head()

# 7- "title" ve "imdbrating" kolonunu içeren ve imdb puanı 2.0 ve 2.0 küçük olan kayıtların 
# ilk 15 tanesini alınız.

# result = df[df["imdbrating"] <= 2.0][["title", "imdbrating"]].head(15)

# 8- Yayın tarihi 2014 ile 2015 arasında olan filmleri listeleyiniz.

result = df[(df["year"] == 2014) | (df["year"] == 2015)]

# 9- Değerlendirme sayısı 10000 den az ve ratingi 2.2 den büyük olanları listeleyiniz

result = df[(df["imdbvotes"] > 10000) & (df["imdbrating"] >= 2.2)][["title", "imdbvotes", "imdbrating"]]

print(result)