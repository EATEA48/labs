#include <stdio.h>
#include <math.h>

int main() {

    float a;
    int x = 3, b = 0;

    printf("Введите число из которого нужно извлечь корень: ");
    scanf("%f", &a);

    while (b != (pow(a, 0.5)))
    {
        b = 0.5 * (x + a / x);
        x = b;
    }
    printf("%d", b);

    return 0;
}

