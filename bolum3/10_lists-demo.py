from unittest import result


autoBrands = ["BMW", "Mercedes", "Opel", "Mazda"]

#1 Kaç eleman vardır ?
# print(len(autoBrands))

#2 Listenin ilk ve son elemanı nedir ?

# firstBrand = print(autoBrands[0])
# lastBrand = print(autoBrands[-1])

#3 Mazda yerine Toyata ekle

autoBrands[-1] = "Toyota"


#4 Mercedes markası listede yer alıyor mu ?

# result = "Mercedes" in autoBrands
# print(result)

#5 Listenin -2 indeksindeki eleman nedir ?

# print(autoBrands[-2])

#6 Listenin ilk 3 elemanını alın.

# print(autoBrands[0:3])

#7 Listenin son 2 elemanını "Toyota" ve "Renault" olarak değiştirin.

# autoBrands[-2:] = ["Toyota", "Renault"]
# print(autoBrands)

#8  Listenin sonuna "Audi" ve "Fiat" değerlerini ekleyin.

autoBrands = autoBrands + ["Audi","Fiat"]
# print(autoBrands)

#9 Listenin son elemanını silin

# del autoBrands[-1]
# print(autoBrands)

#10 Listede 3. değerden itibaren sırasıyla "Honda","Tofaş","Subaru" markalarını ekleyin.

autoBrands = autoBrands[0:2] + ["Honda","Tofaş","Subaru"] + autoBrands[3:]
# print(autoBrands)

#11 Elemanları tersten yazdırın.

print(autoBrands[::-1])