#!/bin/bash
# MIT License Copyright (c) 2021 Jeremias Grym
# version 0.2.2

function help_text() {
    echo "Usage: passgen [OPTION] [LENGTH]"
    echo "Default length is 12, but 4 for digits"; echo
    echo "-d, --pin     for digits only; useful for generating PIN or similar"
    echo "-c, --letter  for letters only, both UPPER- and lowercase"
    echo "-p, --pass    for digits, letters and special characters !@#$%&+?"; echo
    exit 1
}

#with no arguments, default to length 12 with uppercase, lowercase and numbers
#with --help as only argument, print help text
if [ -z $1 ]
then
    random=$(cat /dev/urandom | tr -dc '0-9A-Za-z' | head -c 12)
    echo $random
    exit 1
elif [ $1 = '--help' ]
then
    help_text
fi

#default to length 12 if no LENGTH is specified
if [ -z $2 ]
then
    length=12
else
    length=$2
fi

#default to length 4 for digits-only
if [ $1 = '-d' ] || [ $1 = '--pin' ]
then
    if [ -z $2 ]
    then
        length=4
    else
        length=$2
    fi
    random=$(cat /dev/urandom | tr -dc '0-9' | head -c $length)
elif [ $1 = '-c' ] || [ $1 = '--letter' ]
then
    random=$(cat /dev/urandom | tr -dc 'A-Za-z' | head -c $length)
elif [ $1 = '-p' ] || [ $1 = '--pass' ]
then
    random=$(cat /dev/urandom | tr -dc '0-9A-Za-z!@#$%&+?' | head -c $length)

#use regex to regenerate passwords until it contains at least one of each:
#lower case, upper case, number, special character
    while ! [[ $random =~ [a-z]+ &&
               $random =~ [A-Z]+ &&
               $random =~ [0-9]+ &&
               $random =~ [\!\@\#\$\%\&\+\?]+ ]]
        do
            random=$(cat /dev/urandom | tr -dc '0-9A-Za-z!@#$%&+?' | head -c $length)
        done

#for unknown options, print the help text
else
    help_text
fi

echo "$random"

