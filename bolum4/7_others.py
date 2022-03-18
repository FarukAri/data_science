# Identity Operator: is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) 
print(x==z) 
print(x is y) # Aynı adreste oldukları için True sonucunu alırız.
print(x is z) # Eşit değerlere sahipler fakat farklı adreslerde olduğu için False sonucunu alırız.
print(x is not z) # x ye z objesi değil midir ? True, değildir.

# Membership Operator : in

x = ['banana', 'apple']
print('banana' in x) # 'banana' x listesi içinde yer alıyor mu?

name = "Faruk"
print("a" in name)
print("a" not in name)