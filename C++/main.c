#include <stdio.h>
#include <stdlib.h>

int main() {

    int* tab = (int*)malloc(10*sizeof(int));

    if (tab == NULL)
    {
        return 1;
    }

    for(int i = 0; i < 10; i++)
    {
        tab[i] = rand() % 100;
    }

    for(int i = 0; i < 10; i++)
    {
        printf("%d ", tab[i]);
    }

    return 0;
}
