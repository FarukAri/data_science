#1 Value Types

x=5
y=8

x=y

y=20

print(x,y) #Yapılan değişiklikten etkilenmez.

#2 Reference Types

list1 = [1, 2, 3, 4]
list2 = []
list2 = list1

list1[0] = 8

print(list1, list2) #Bu durumda 2 adet kaynak olmaz tek bir kaynak olur, o yüzden yapılan değişiklerden ikisi de etkilenir.
