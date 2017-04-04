/*
Find the greatest common divisor of two nonnegative values.
Invented by Euclides around 300 B.C.
*/
#include <stdio.h>

int main(void) {
    int a, b, temp;

    printf("Enter two integers: ");
    scanf("%i%i", &a, &b);

    while ( b != 0 ) {
        temp = a % b;
        a = b;
        b = temp;
    }

    printf("Their greatest common divisor is %i\n", a);

    return 0;
}
