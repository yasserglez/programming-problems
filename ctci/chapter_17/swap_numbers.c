/* Interview Question 17.1 */

#include <stdio.h>
#include <stdlib.h>

void swap_numbers(int *a, int *b)
{
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

int main(void)
{
    int a, b;

    while (fscanf(stdin, "%d %d", &a, &b) > 0) {
        swap_numbers(&a, &b);
        printf("%d %d\n", a, b);
    }

    return EXIT_SUCCESS;
}
