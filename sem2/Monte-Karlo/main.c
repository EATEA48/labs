#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main()
{
    int i,n1=1000,n2=0,n0=0,p;
    float a,b,m,np;
    double Pi;
    np=n1*0.1;
    srand (500);
    for (i=1;i<=n1;i++)
    {
        a = rand() % 100 * 0.01;
        b = rand() % 100 * 0.01;
        m = a*a+b*b;
        printf ("%f %f %f %d \n", a,b,m,n2);
        if (m<=1)
        {
            n2++;
        }
    }

    Pi = (double)4 * n2 / n1;
    printf ("Pi = %f\n",Pi);
    return 0;
}
