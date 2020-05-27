/* MIT License Copyright 2020 Jeremias Grym */

/* Enkelt program för att räkna ut hur många folköl 3.5% eller nubbar sprit 
    som starköl eller vin motsvarar. Folkisar motsvarar mer än man tror!
*/

#include <stdio.h>

int main(void) {
    float folkis = 50 * 0.035;
    float shot = 4 * 0.04;

    float burk, stark;
    float alko, folk_ratio, shot_ratio;

    printf("Hur stor burk eller flaska har du? [cl] ");
    scanf("%f", &burk);
    printf("Hur stark är den? [vol%%] ");
    scanf("%f", &stark);

    alko = burk * (stark / 100);
    folk_ratio = alko / folkis;
    shot_ratio = alko / shot;

    printf("\nDet motsvarar %.2f centiliter ren alkohol\n", alko);
    printf(" eller %.2f burkar (50 cl) folköl 3.5%%\n" ,folk_ratio);
    printf(" eller %.2f st (4 cl) shots 40%%\n" ,shot_ratio);

    return 0;
}
