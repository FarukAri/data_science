list = [1, 2, 3]

tuple = (1, "iki", 3)

print(type(list))
print(type(tuple))

# Tuple içinde yer alan bir elemanı sonradan değiştiremezsin. 
# Tuple için sadece .count ve .index methodları kullanılabilir.
# Tuple elemanları toplanabilir.

names = ("Ronaldo", "Messi", "Magnus")

names = names + tuple
print(names)