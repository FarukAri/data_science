# 1- Sayıları yazdır

# numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# i = 0

# while i<=7 :
#     x = numbers[i]
#     print(x)
#     i = i + 1

#############################################################################################################

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan aldığın sayıların arasındaki tek sayıları yazdır.

# a = int(input('1. sayıyı giriniz: '))
# b = int(input('2. sayıyı giriniz: '))

# if a>b:
#     i = b
#     while b <= i <= a:
#         if (i %2 == 1):
#             print(i)
#         i = i + 1
# else:
#     i = a
#     while a <= i <= b :
#         if (i %2 == 1):
#             print(i)
#         i = i + 1

#############################################################################################################

# 3- 1-100 arasındaki sayıları tersten yazdırın.

# i = 100

# while 0 <= i <= 100 :
#     print(i)
#     i = i - 1

#############################################################################################################

# 4- Kullanıcıdan aldığınız 5 sayıyı sıralı şekilde yazdırın.

# numbers = []

# i = 0

# while i < 5 :
#     sayi = int(input("Bir sayı giriniz: "))
#     numbers.append(sayi)
#     i += 1

# numbers.sort()
# print(numbers)

#############################################################################################################

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesine ekleyin
#   ** ürün sayısını kullanıcıya sorun
#   ** dictionary listesi yapın, ("name","price") şeklinde olsun

urunler = []

i = 0

urunSayisi = int(input("Lütfen ürün sayısını giriniz: "))

while i < urunSayisi :
    name = input("Ürünün ismini giriniz: ") 
    price = input("Ürünün fiyatını giriniz: ")
    urunler.append({
        "ad" : name,
        "fiyat" : price
    })
    i += 1

for x in urunler:
    print(f'Ürünün adı: {x["ad"]}, ürünün fiyatı: {x["fiyat"]}')
