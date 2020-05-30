#include <math.h>
#include <stdio.h>
#define FCN_A_COST 1
#define IDEAL_INTEGRAL_VALUE 42
#define pi 3.14
double f1(double,double );
double freq(double);

double rectIntegral(double , double , int );
double trapIntegral(double, double, int );
double simpIntegral(double, double, int );
void absDifferenceCompare(int, int, int, double, double );
int main()
{
    printf("Ideal integral value: 42\n");
    absDifferenceCompare(100, 1000, 100, 1, 2);
    printf("Rect integral value: %lf\n",rectIntegral(1,2,100));
    printf("Trap integral value: %lf\n",trapIntegral(1,2,100));
    printf("Simp integral value: %lf\n",simpIntegral(1,2,100));
    return 0;
}
double rectIntegral(double a, double b,int n)
{
    return (sin(pi * (10 * pow(a, 2) + 37 * a * b + 7 * pow(b, 2)))) + a;
}
double trapIntegral(double a, double b,int N)
{
    return (sin(pi * (10 * pow(a, 2) + 37 * a * b + 7 * pow(b, 2)))) + a-b;
}
double simpIntegral(double a, double b,int N)
{
    return (sin(pi * (10 * pow(a, 2) + 37 * a * b + 7 * pow(b, 2)))) + a+b;
}

double f1(double x,double a)
{
    return x*x+a;
}
double freq(double time)
{
    return 1/ time;
}
void absDifferenceCompare(int startN, int stopN,int stepN ,double a, double b)
{
    for(int N = startN;N <= stopN;N+=stepN)
    {
        printf("%d;%lf;%lf;%lf\n,",N,
        fabs(IDEAL_INTEGRAL_VALUE-rectIntegral(a,b,N)),
        fabs(IDEAL_INTEGRAL_VALUE-trapIntegral(a,b,N)),
        fabs(IDEAL_INTEGRAL_VALUE-simpIntegral(a,b,N)));
    }
}
