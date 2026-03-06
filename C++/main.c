#include <stdio.h>
#include <mylib.h>

int main(void) {

    byte y = 4;
    transform((byte*) &y);
    printf("%d", y);

    return 0;
}
