

x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6

#1 Kullanıcıdan alınan iki sayı ile x, y, z sayılarının toplamının farkı nedir ? 

# firstNumber = input("1. sayı: ")
# secondNumber = input("2. sayı: ")

# sum1 = int(firstNumber) * int (secondNumber)
# sum2 = int(x) + int(y) + int(z)

# result = sum1 - sum2
# print(result)

#2 y nin x e kalansız bölümünü hesaplayınız.

# result = y // x
# print(result)

#3 ( x, y, z) toplamının mod 3 ü nedir ?

# sum = x+y+z
# result = sum % 3
# print(result)

#4 y nin x. kuvvetini hesaplayınız

# result = y**x
# print(result)

#5 x, *y, z = numbers işlemine göre z nin küpü kaçtır

# x, *y, z = numbers
# result = z**3
# print(result)

#6 x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır

x, *y, z = numbers
result = y[0] +y[1] + y[2]
print(result)
