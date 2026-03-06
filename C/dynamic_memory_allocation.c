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

    printf("\n");

    int* newtab = (int*)realloc(tab, 20*sizeof(int));

    if (newtab == NULL)
    {
        return 1;
    }

    for(int i = 10; i < 20; i++)
    {
        newtab[i] = 0;
    }

    for(int i = 0; i < 20; i++)
    {
        printf("%d ", newtab[i]);
    }

    return 0;
}
