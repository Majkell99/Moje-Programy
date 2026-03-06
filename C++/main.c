#include <stdio.h>

int pierwsza(int n, int dzielnik)
{
    if(n % dzielnik == 0)
    {
        return 0;
    }

    return pierwsza(n, dzielnik + 1);
}

int main()
{
    if(pierwsza(6) == 0)
    {
        printf("Nie pierwsza");
    }
    else
    {
        printf("Pierwsza");
    }

    return 0;
}
// NIE WIEM