# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteiyp ehliyet alabilme durumunu kontrol ediniz. 
#    Lise veya üni mezunu ve 18 yaşından büyük olmalıdır.

# isim = input("İsminizi girin: ")
# yas = int(input("Yaşınız girin: "))
# egitimBilgisi = input("Eğitim bilginizi girin: ")

# if yas >= 18 :
#     if ((egitimBilgisi == "Üniversite") or (egitimBilgisi == "Lise")):
#         print("Ehliyet almak için gerekli koşulları sağlıyorsunuz.")
#     else :
#         print("Eğitim durumunuz ehliyet almak için yeterli değildir.")
# else :
#     print("Yaşınız ehliyet almak için yeterli değildir.")

# 2- Bir öğrencinin 3 sınavdan aldığı puanın ortalamasını alıp, notunu belirleyiniz.
# 0-24 = 0      25-44 = 1       45-54 = 2       55-69 = 3       70-84 = 4       85-100 = 5

# sinav1 = float(input("1. sınavınızın notunu girin: "))
# sinav2 = float(input("2. sınavınızın notunu girin: "))
# sinav3 = float(input("3. sınavınızın notunu girin: "))

# ortalama = (sinav1 + sinav2 + sinav3)/3

# if 0<= ortalama <= 24 :
#     print("Notunuz 0'dır.")
# elif 25<= ortalama <= 44 :
#     print("Notunuz 1'dir.")
# elif 45<= ortalama <= 54 :
#     print("Notunuz 2'dir.")
# elif 55<= ortalama <= 69 :
#     print("Notunuz 3'dür.")
# elif 70<= ortalama <= 84 :
#     print("Notunuz 4'dür.")
# else :
#     print("Notunuz 5'dir.")

# 3- Trafiği çıkış tarihi alınan bir aracın servis zamanını hesaplayınız.

import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı (Yıl/Ay/Gün): ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1. servis aralığı: ")
elif 365<days<=(365*2):
    print("2. servis aralığı: ")
elif 365*2<days<=(365*3):
    print("3. servis aralığı: ")
else:
    print("Hatalı tarih")

  


