maasAli = 5000
maasAyse = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAyse - (maasAyse * vergi))

# Değişken Tanımlama Kuralları

# rakam ile başlayamaz

number1 = 15
print (number1)

number1 +=20
print (number1)

# büyük küçük harf duyarlılığı vardır

age=28
AGE=32

print(age)
print(AGE)

# Türkçe karakter kullanılmaz

x = 1               # int
y = 2.5             # float
name = "Masa"       # string
isStudent = True    # bool  

x, y , name, isStudent = (1, 2.5, "Masa", True) # Tek satırda tanımlama

firstName = "Faruk"
lastName = " Arı"
print(firstName + lastName) # Faruk Arı