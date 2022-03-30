import pandas as pd

df = pd.read_csv("datasets/GBvideos.csv")

# 1- İlk 10 kaydı getiriniz.

result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.

result = df[5:10].head(5)

# 3- Kolon isimlerini ve sayılarını bulunuz.

result = df.columns
result = len(df.columns)

# 4- İstenilen kolonları siliniz.

result = df.drop(["thumbnail_link", "comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1)

# 5- Like ve dislike sayılarının ortalamasını bulunuz.

result = df[["likes","dislikes"]].mean()

# 6- İlk 50 videonun like ve dislike kolonlarını getiriniz.

result = df[["likes","dislikes"]].head(50)

# 7- En çok görüntülenen video hangisidir?

result = df[df["views"] == df["views"].max()]["title"]

# 8- En fazla götüntülenen 10 video hangisidir?

result = df.sort_values("views", ascending=False)["title"].head(20)

# 9- Kategoriye göre beğeni ortalamalarını sıralayınız.

result = df.groupby("category_id").mean().sort_values("likes", ascending= False)["likes"]

# 10- Kategori id ye göre yorum sayılarını yukarıdan aşağıya doğru sıralayınız.

result = df.groupby("category_id").sum().sort_values("comment_count", ascending= False)["comment_count"]

# 11- Her kategoride kaç video vardır?

result = df["category_id"].value_counts()

# 12- Her videonun title uzunluğu yeni bir kolonda gösterilsin.

df["title_len"] = df["title"].apply(len)
result = df

# 13- Her video için kullanılan tag sayısını yeni bir kolona yazdırınız.

df["tag_counts"] = df["tags"].apply(lambda x: len(x.split("|")))

# or

def tagCount(tag):
    return len(tag.split("|"))

df["tag_counts"] = df["tags"].apply(tagCount)

# 14- (Like/(Dislike+Like)) oranına göre videoların beğenilme oranını hesapla, yeni kolona yazdır.

def likedislikerate(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    list1 = list(zip(likesList,dislikesList))

    rateList = []

    for like,dislike in list1:
        if (like+dislike) == 0:
            rateList.append(0)
        else:
            rateList.append(like/(dislike+like))

    return rateList
        
df["like_dislike_rate"] = likedislikerate(df)

result = df.sort_values("like_dislike_rate", ascending=False)[["title","likes","dislikes","like_dislike_rate"]]

print(result)