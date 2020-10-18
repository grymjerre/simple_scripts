#!/bin/python3

# MIT License Copyright 2019 Jeremias Grym

print("Ytterligare en ny sparsnurra!")
print("Denna räknar ut tid till ett sparmål.")
start = int(input("Hur mycket börjar du med: "))
ranta = float(input("Ränta på kontot i procent: "))
spara = int(input("Hur mycket vill du spara per månad: "))
mal = int(input("Vad är ditt sparmål: "))

summa = start
counter = 0
nuranta = 0
sumspar = 0
sumranta = 0
tid = 0
while summa <= mal:
        nuranta = (summa+spara) * (ranta/100.0)/12        
        summa += spara + nuranta
        sumspar += spara
        sumranta += nuranta
        tid += 1
ar = tid / 12

print("\nDet tar dig ca %d månader (%.2f år) att nå ditt mål på %d kronor." % (tid, ar, mal))
print("Du har då själv sparat %d kronor och fått %.2f kronor i ränta." % (sumspar, sumranta))
