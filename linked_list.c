// Programming in C, Ch. 10 Pointers

#include <stdio.h>

int main (void)
{
    struct entry {
        int value;
        struct entry *next; // pointer to the structure itself
    };

    struct entry n1, n2, n3;
    struct entry *list_pointer = &n1; // start of the linked list

    n1.value = 1;
    n1.next = &n2;

    n2.value = 2;
    n2.next = &n3;

    n3.value = 3;
    // Mark list end with null pointer
    // - constant 0 casted to the "pointer to struct entry" type.
    n3.next = (struct entry *) 0;

    while ( list_pointer != (struct entry *) 0 ) {
        printf("%i\n", list_pointer->value); // or (*list_pointer).value
        list_pointer = list_pointer->next;
    }
}
