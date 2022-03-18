
'''
ogrenciler = {
    "120" : {
        "ad" : "Ali",
        "soyad":"Yılmaz",
        "telefon" : "532 000 00 01",
    },
    "125" : {
        "ad" : "Can",
        "soyad" : "Korkmaz",
        "telefon" : "532 000 00 02",
    },
    "128" : {
       "ad" : "Volkan",
        "soyad" : "Yükselen",
        "telefon" : "532 000 00 03", 
    },
}
'''

ogrenciler = {}

number1 = input("Öğrenci no : ")
name1 = input("Öğrenci adı : ")
surname1 = input ("Öğrenci soyadı : ")
phone1 = input ("Öğrenci telefon no : ")

# 1. YÖNTEM


number2 = input("Öğrenci no : ")
name2 = input("Öğrenci adı : ")
surname2 = input ("Öğrenci soyadı : ")
phone2 = input ("Öğrenci telefon no : ")

number3 = input("Öğrenci no : ")
name3 = input("Öğrenci adı : ")
surname3 = input ("Öğrenci soyadı : ")
phone3 = input ("Öğrenci telefon no : ")




ogrenciler[number1] = {
        "ad" : name1 ,
        "soyad" : surname1 ,
        "telefon" : phone1 ,
}

ogrenciler[number2] = {
        "ad" : name2 ,
        "soyad" : surname2 ,
        "telefon" : phone2 ,
}

ogrenciler[number3] = {
        "ad" : name3 ,
        "soyad" : surname3 ,
        "telefon" : phone3 ,
}


# 2. YÖNTEM
'''
ogrenciler.update ({
    number1 : {
        "ad" : name1,
        "soyad" : surname1,
        "telefon" : phone1
    }
}) 
'''

print("*"*50)

ogrNo = input("Öğrenci no: ")
ogrenci = ogrenciler[ogrNo]

print(f'Aradığınız {ogrNo} nolu öğrencinin adı {ogrenci["ad"]} soyadı {ogrenci["soyad"]} ve telefon numarası {ogrenci["telefon"]}')