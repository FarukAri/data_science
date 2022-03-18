
username = "Legendari"
password = "12345"

a = input("Kullanıcı adınız girin: ")
b = input("Şifrenizi girin: ")

# isLoggedIn = (a == username) and (password == b)

# if isLoggedIn:
#     print("******HOŞGELDİNİZ******")

# else:
#     print("Girmiş olduğunuz kullanıcı adı veya şifre hatalıdır. Lütfen tekrar deneyiniz.")

if (username == a):

    if (password == b):
        print(("HOŞGELDİNİZ").center(100,"*"))
    else:
        print("Girmiş olduğunuz parola hatalıdır.")

else:
    print("Girmiş olduğunuz kullanıcı adı veya şifre hatalıdır. Lütfen tekrar deneyiniz.")