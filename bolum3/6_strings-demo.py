website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

lengthWebsite = len(website)
lengthCourse = len(course)

print("Q1: ", lengthCourse)
print("Q2: ", website[7:10])
print("Q3: ", website[(lengthWebsite-3):(lengthWebsite)])
print("Q4: ", course[:15])
print("Q5: ", course[(lengthCourse - 15):])
print("Q5_2: ", course[-15:-1])
print("Q6: ", course[::-1])

s = "12345"*5
print(s[::5])

#7

name, surname, age, job = "Faruk", "Ari", 26, "Mechanical Engineering"

result = "This is " + name + " " + surname + ". My age is "+ str(age)+ ". I am a "+ job
print(result)

result2 = "This is {} {} .I am {} years old . I am a {}".format (name, surname, age, job)
result3 = "This is {1} {0} .I am {3} years old . I am a {2}".format (name, surname, age, job)
result4 = f"This is {name} {surname} .I am {age} years old . I am a {job}"
print(result2)
print(result3)
print(result4)

#8
r = "Hello moto"
r = r[0:6]+"f"+r[7:]
print(r)
