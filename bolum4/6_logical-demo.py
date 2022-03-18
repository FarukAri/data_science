
# 1- Girilen bir sayının 0-100 arasında olup olmadığını sorgulayınız.

# a = float(input("Bir sayı giriniz: "))

# result = (a>0) and (a<100)
# print(f'Is number between 0 and 100 ? : {result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını sorgulayınız.

# a = int(input("Bir sayı giriniz: "))

# result = (a % 2 == 0) and (a>100)
# print(f'Is number positive and even number ? : {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = "farukari@gmail.com"
# password = "12345"

# a = input("Mail adresinizi girin: ")
# b = input("Şifrenizi girin: ")

# result = (email == a) and (password == b)
# print(f"Girdiğiniz email veya şifreniz: {result}")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input("1. sayı: "))
# b = int(input("2. sayı: "))
# c = int(input("3. sayı: "))

# result1 = (a>b) and (a>c)
# result3 = (c>b) and (a<c)
# result2 = (b>c) and (b>a)
# print(f"1. number is the highest number: {result1}")
# print(f"2. number is the highest number: {result2}")
# print(f"3. number is the highest number: {result3}")

# result4 = (a<b) and (a<c)
# result6 = (c<b) and (a>c)
# result5 = (b<c) and (b<a)

# print(f"1. number is the lowers number: {result4}")
# print(f"2. number is the lowest number: {result5}")
# print(f"3. number is the lowest number: {result6}")

# 5- Kullanıcıdan 2 vize (%60) ve 1 final (%40) notunu alıp ortalama hesaplayınız. ##
# Eğer ortalama 50 den büyük değilse kaldı yazdırınız.
# Finalde geçer not 50 ve üstü, eğer 70 ve üstü alırsa direk geçer.

a = float(input ("1. vize notunuz giriniz: "))
b = float(input ("2. vize notunu giriniz: "))
c = float(input ("Final notunu giriniz: "))

sum = (a*0.3) + (b*0.3) + (c*0.4)
result1 = (a*0.3) + (b*0.3) + (c*0.4) >= 50
result2 = (result1) and (c>=50)
result3 = (result2) or (c>=70)
print(f'Not ortalamanız : {sum}, dersi geçme durumunuz : {result3}')