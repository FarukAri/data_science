from re import X


r = float(input ("Yarı çap (cm) =  "))
pi = 3.14

daireAlani = ( pi * (int(r))**2)
daireCevresi = (2*(pi)*(int(r)))

print("Daire Alanı = ", str(daireAlani)," Daire Çevresi = ", str(daireCevresi))