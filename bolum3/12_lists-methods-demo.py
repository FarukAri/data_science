from turtle import clear


names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

#1 "Cenk" değerini listenin sonuna ekleyin.

# names.append("Cenk")
# print(names)

#2 "Sena" değerini listenin başına ekleyiniz.

# names.insert(0,"Sena")
# print(names)

#3 "Deniz" ismini listeden siliniz.

# names.remove("Deniz") 
# or 
# names.pop(3)
# print(names)

#4 "Deniz" isminin indeksi kaçtır?

# indexDeniz = names.index("Deniz")
# print(indexDeniz)

#5 "Ali" listenin bir elemanı mıdır?

# infoAli = "Ali" in names
# print(infoAli)

#6 "names" liste elemanlarını ters çevir.

# names.reverse()
# print(names)

#7 "names" liste elemanlarını alfabetik olarak sıralayınız.

# names.sort()
# print(names)

#8 "years" liste elemanlarını sayısal büyüklüğe göre sıralayınız.

# years.sort()
# print(years)

#9 str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz

# str = "Chevrolet,Dacia"
# result = str.split(",")
# print(result)

#10 "years" dizisinin en büyük ve en küçük elemanları nedir ?

# yearsMin = min(years)
# yearsMax = max(years) 
# print(yearsMin, yearsMax)

#11 "years" dizisinde kaç tane 1998 değeri vardır?

# value1998 = years.count(1998)
# print(value1998)

#12 "years" dizisinin tüm elemanlarını siliniz.

# years.clear()
# print(years)

#13 Kullanıcıdan aldığımız 3 adet markayı liste halinde yazdıralım.

markalar = []
marka1 = input("marka1: ")
markalar.append(marka1)


marka2 = input("marka2: ")
markalar.append(marka2)


marka3 = input("marka3: ")
markalar.append(marka3)

print(markalar)