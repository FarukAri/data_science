
x = 6

# and

result1 = x > 5 and x < 10 # İkisi de doğru ise True verir, biri yanlış ise False verir.
result2 = x > 8 and x < 10 

print (result1, result2)

canHakki = 5
devamTusu = "e"

result3 = (canHakki > 0) and (devamTusu == "e")
print(result3)

# or (İki sorgudan biri doğru ise True çıktısını verir.)

''' 

True-True = True
True-False = True
False-False = False

'''

# not (and operatörünün tersi)

'''
True-True = False
True-False = False
False-False = True

'''

result4 = ((x>4) or (x%2==0)) and (x<10)
print(result4)