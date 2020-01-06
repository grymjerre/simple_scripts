#Copyright Jeremias Grym 2019
#Attribution-NonCommercial-NoDerivs
#CC BY-NC-ND

# -*- coding: utf-8 -*-

folkis = 50 * 0.035
shot = 4 * 0.4

burk = int(input("Hur stor burk eller flaska har du? [cl] "))
stark = float(input("Hur stark är den? [vol %] "))

alko = burk * (stark / 100)
folk_ratio = alko / folkis
shot_ratio = alko / shot

print("\nDet motsvarar %.2f centiliter ren alkohol" % (alko))
print(" eller %.2f burkar folköl 3.5%%" % (folk_ratio))
print(" eller %.2f st shots 40%%" % (shot_ratio))

