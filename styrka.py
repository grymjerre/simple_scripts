#!/usr/bin/python3

# MIT License Copyright 2019 Jeremias Grym
# Enkelt program för att jämföra valfri alkoholhaltig dryck med folköl eller sprit

folkis = 50 * 0.035
shot = 4 * 0.4

burk = float(input("Hur stor burk eller flaska har du? [cl] "))
stark = float(input("Hur stark är den? [vol %] "))

alko = burk * (stark / 100)
folk_ratio = alko / folkis
shot_ratio = alko / shot

print("\nDet motsvarar %.2f centiliter ren alkohol" % (alko))
print(" eller %.2f burkar (50 cl) folköl 3.5%%" % (folk_ratio))
print(" eller %.2f st (4 cl) shots 40%%" % (shot_ratio))

