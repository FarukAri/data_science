
fruits = { "orange" , "banana" , "apple" }

# print(fruits[0]) indekslenemez

# for x in fruits :
#     print(x)

fruits.add("cherry")
#print(fruits)

fruits.update(["mango" , "watermelon"]) #Var olan elemanı setin içine tekrar ekleyemezsin.
# print(fruits)

numbers = [1 ,2 ,3 ,6 ,2 , 13, 232,24,2,7,3,1,2]
print(numbers)
print(set(numbers)) #Setlerde tekrar eden değerler printte yer almaz.

fruits.remove("banana")
print(fruits)

fruits.discard("apple")
print(fruits)

fruits.pop() #Elemanlar numaralanmadığı için son numaralı eleman olmaz, o yüzden rastgele bir eleman siler.
print(fruits)

fruits.clear #Tüm elemanları siler.