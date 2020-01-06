#Copyright Jeremias Grym 2019
#Attribution-NonCommercial-NoDerivs
#CC BY-NC-ND

#!/bin/bash
echo -n > hyra

if [ "$1" == "" ]; then
        mypath="/storage/Documents/_hyresavi/"
else
        mypath="$1"
fi

for filename in "$mypath"*.pdf; do
    pdfgrep Totalt "$filename" | awk '{print $5,$8 $9}' >> hyra;
done

awk 'BEGIN {sum = 0; c = 0}
	{sum += $2; c++	}
    END {print "Summa: " sum "\n" "Snitt: " sum/c}' ./hyra >> hyra;
