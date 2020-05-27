/* MIT License Copyright 2020 Jeremias Grym */

#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 100; i++) {
        //Alt: i%3 && i%5 -> skriv FizzBuzz här och annat värde på slutet
        if (i%3!=0 && i%5!=0) {
            printf("%d", i);
        } else {
            if (i % 3 == 0)
                printf("Fizz");
            if (i % 5 == 0)
                printf("Buzz");
        }
        printf("\n");
    }
}
