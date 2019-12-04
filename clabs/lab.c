#include <stdio.h>


int main() {
    float a[40];
    float x[40];
    char fun;
    int p;
    float sh;

    scanf("%f", a);
    scanf("%f", x);
    scanf("%s", fun);
    scanf("%i", p);
    scanf("%f", sh);


    while (1){
        while (p >= 0){
            if (p == 0 ){
                char question;
                printf("Вы хотите продолжить?(yes, no): ");
                scanf("%s", question);
                if (question == 'yes'){
                    printf("Сколько считать?: ");
                    scanf("%i", p);
                    printf("С каким шагом?: ");
                    scanf("%f", sh);
                }
                else{
                    printf("END");
                }
            }
            if (a != 0 && a != x){
                if (fun == "g"){
                    for i in range(p){
                        g = (-1*(2*(-5*a**2 + 3*a*x + 2*x**2) / (5*a**2 + 9*a*x - 2*x**2)))
                        if  ((5*a**2 + 9*a*x - 2*x**2) == 0){
                            print("ERROR")
                            else
                        }

                    }
                }
            }

        }

        return 0;
    }

    return 0;
}