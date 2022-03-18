
name = 'Faruk Arı'

# for letters in name:
#     if letters == 'k':
#         break             # 'k' harfine geldiğimizde döngüyü durdurur.
#     print(letters)

# for letters in name:
#     if letters == 'k':
#         continue            # 'k' harfinin olduğu döngüyü atlar ve devam eder.
#     print(letters)


# x = 0

# while x<5:
#     x += 1          # Eğer arttırma işlemi sonda olsaydı, continuedan sonra hemen başa döneceği için 2 de takılı kalırdı.
#     if x == 2:
#         continue
#     print(x)

# 100 e kadar olan çift sayıların toplamı

a = 0
result = 0

while a <= 100:
    a += 1
    if a%2 == 1:
        continue
    result += a

print(result)