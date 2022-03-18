from unittest import result


website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1 "   Hello Moto  " karakter dizinin başındaki ve sonundaki boşlukları sil

# index = "     Hello Moto   "
# index = index.strip()

#2 "http://www.sadikturan.com" içindeki sadikturan dışındaki bütün karakterleri silin.

# website = website.strip("htp:/w.com")
# print(website)

#3 "course" karakter dizisinin tüm harflerini küçük harf yap

# course = course.lower()
# print(course)

#4 "website" içinde kaç tane a harfi vardır?

# info_1 = website.count("a")
# info_2 = website.count("www")
# info_3 = website.count("a",0,20) # 0-20 karakterleri arasında istenilen karakter kaç tane var ?
# print(info_1)

#5 "website" www ile başlayıp com ile bitiyor mu?

# index = website.startswith("www")
# index_2 = website.endswith("com")

# print(index)
# print(index_2)

#6 "website" ifadesi içinde ".com" var mı?

# result = website.find("com")
# result = website.find("com",0,10)  # 0-10 karakterleri arasında istenilen karakter var mı ?
# result_2 = course.rfind("Python") # Sağdan karakter sayımına başlanır
# print(result)
# print(result_2)

#7 "course" içerisindeki karakterler alfabetik mi ?

# result = course.isalpha() # Alfabetik mi ?
# print(result)
# result_2 = course.isdigit() # Karakterle rakam mı ?
# print(result_2)

#8 "Contents" "*" ekleyerek 50 karakter yap.

# result = "Contents".center(100,"*")
# print(result)

#9 "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin

# result = course.replace(" ", " aq ")
# result = course.replace(" ", " aq ", 5) # İlk 5 karakterin değişimini yapar
# print(result)

#10 "Selam Dünyalı" karakter dizisindeki "Selam" ifadesini "Selamun Aleyküm" ile değiştirin

# index = "Selam Dünyalı"
# result = index.replace("Selam","Selamun Aleyküm")
# print(result)

#11 "course" karakter dizisini boşluklardan ayırın

# result = course.split(" ")
# print(result)