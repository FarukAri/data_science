
## 1) Girilen 2 sayıdan hangisi daha büyüktür ##

# a = int (input("1. sayı: "))
# b = int (input("2. sayı: "))

# result = a > b
# print (f'a: {a} b : {b} den büyüktür : {result}')

## 2) Kullanıcıdan 2 vize (%60) ve 1 final (%40) notunu alıp ortalama hesaplayınız. ##
# Eğer ortalama 50 den büyük değilse kaldı yazdırınız

# a = int(input ("1. vize notunuz giriniz: "))
# b = int(input ("2. vize notunu giriniz: "))
# c = int(input ("Final notunu giriniz: "))

# result = (a*0.3) + (b*0.3) + (c*0.4)
# print(f'Not ortalamanız : {result}, dersi geçme durumunuz : {result >= 50}')

## 3) Girilen bir sayının tek mi çift mi olduğunu yazdırın. ##

# a = int(input("Bir sayı giriniz: "))
# tekcift = a % 2 == 0
# print(f"Girdiğiniz sayı çifttir : {tekcift}")

## 4) Girilen sayının pozitif-negatif durumuna bakınız. ##

# a = float(input("Bir sayı giriniz: "))
# result = a > 0
# result2 = a < 0
# input(f'Girdiğiniz sayı pozitif mi : {result} // Girdiğiniz sayı negatif mi : {result2}')

## 5) Parola ve email bilgisi isteyip doğruluğunu kontrol et. ##

email = "farukari.@gmail.com"
password = "12345"

a = input("Mail adresiniz girin: ")
b = input("Şifrenizi girin: ")

result1 = a == email.strip() # Boşlukları silmek için
result2 = b == password.strip()

print(f'Girilen email adresi: {result1}, girilen parola: {result2}')