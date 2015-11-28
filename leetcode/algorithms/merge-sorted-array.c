/* https://leetcode.com/problems/merge-sorted-array/ */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void merge(int *num1, int n, int *num2, int m)
{
    int i = 0, j = 0, k = 0;

    while (i < n && j < m) {
        if (num1[k] > num2[j]) {
            memmove(&num1[k + 1], &num1[k], (n + m - k - 1) * sizeof(int));
            num1[k] = num2[j];
            j++;
        } else {
            i++;
        }
        k++;
    }

    if (i == n && j < m) {
        memcpy(&num1[k], &num2[j], (m - j) * sizeof(int));
    }

}

int main(void)
{
    int i;
    int n = 4, m = 4;
    int num1[] = { 0, 1, 5, 10, 0, 0, 0, 0 };
    int num2[] = { 2, 3, 6, 9 };

    merge(num1, n, num2, m);

    for (i = 0; i < n + m; i++) {
        printf("%d\n", num1[i]);
    }

    return EXIT_SUCCESS;
}
