// Reverse the digits of a number

#include <stdio.h>

int main(void)
{
    int number, right_digit;

    printf("Enter a number: ");
    scanf("%i", &number);

    do {
        right_digit = number % 10;
        printf("%i", right_digit);
        number = number / 10; // integer division
    } while ( number != 0 );

    printf("\n");

    return 0;
}
