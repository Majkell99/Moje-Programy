#include <stdio.h>

int binarna(int n)
{
    if(n == 0)
    {
        return 0;
    }
    else
    {
        binarna(n / 2);
        printf("%d", n % 2);
    }
}

int main() {

    binarna(20);
    return 0;
}
