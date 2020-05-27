#!/usr/bin/bash

# MIT License Copyright 2020 Jeremias Grym
# Läser lönespec som pdf och plockar ut beloppet för att räkna ut snittlönen på specarna i katalogen

echo -n > salary

if [ "$1" == "" ]; then
        mypath="/storage/Documents/_payslip/"
else
        mypath="$1"
fi

for filename in "$mypath"*.pdf; do
    pdftotext "$filename" - | tac | awk 'NF>1{sub(/[*\f]/, "");print$1$2}' | head -n 1 >> salary;
done

awk 'BEGIN {sum = 0; c = 0}
	{sum += $1; c++	}
    END {print "Summa: " sum "\n" "Snitt: " sum/c}' ./salary >> salary;

