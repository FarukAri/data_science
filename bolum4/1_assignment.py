
x, y, z = 5, 10, 17

#x, y= y, x

print(x, y, z)

# x += 5      # x = x + 5
# x -= 5      # x = x - 5
# x *= 5      # x = x * 5
# x /= 5      # x = x / 5
# x //= 5     # x = x // 5 (Sonucu tam sayı verir. Örn : 17 // 5 = 3)
# x %= 2      # x = x % 2 ( Modunu alır. )
x**= 5      # x = x^5  
print(x, y, z)

values = 1, 3, 7 
print(type(values))

x, y, z= values         # values = 1, 3 olsaydı atama olmazdı çünkü z değerinin karşılığı bulunmamaktadır. Hata verir.
print(x, y, z)

values2 = 1, 3, 5, 8, 9
x, y, *z = values2      # z nin başında yıldız bulunduğu için fazla elemanlarla z de bir liste oluşturulur. Eğer yıldız olmasaydı hata verirdi.
print (x, y, z)
print(x, y, z[1])