
numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- Sayılar listesindeki hangi sayılar 3 ün katıdır ?

# for x in numbers:
#     if x%3 == 0:
#         print(x)

#############################################################################################################

# 2- Sayılar listesindeki sayıların toplamı kaçtır ?

# sum = 0

# for x in numbers:
#     sum = sum + x

# print(sum)

#############################################################################################################

# 3- Sayılar listesindeki tek sayıların karesi kaçtır ?

# sum = 0

# for x in numbers:
#     if x%2 == 1:
#         y = x**2
#         sum = sum + y

# print(sum)

#############################################################################################################

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# for x in sehirler:
#     if (len(x)) <= 5:
#         print(x)

#############################################################################################################

# 5- Ürünlerin fiyatların toplamı nedir ?

smartphones = [

    {'name' : 'samsung S6', 'price' : '3000'},
    {'name' : 'samsung S7', 'price' : '4000'},
    {'name' : 'samsung S8', 'price' : '5000'},
    {'name' : 'samsung S9', 'price' : '6000'},
    {'name' : 'samsung S10', 'price' : '7000'},

]

sum = 0

for a in smartphones :
   b = int(a['price'])
   sum += b

print(sum)

for x in smartphones :
    if (int(x['price'])) <= 5000 :
        print(x['name'])