#include <stdio.h>

int main() {
    float S = 7;
    float x = 5;

    float x1;

    do {
        x1 = (x + (S / x)) / 2;

        x = x1;

    } while ((x1 - x) > 0.0001);

    printf("%f", x1);

    return 0;
}
