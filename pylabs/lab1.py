
from math import *

a = float(input("Введите a: "))
x = float(input("Введите x: "))
fun = str(input("Введите ф-ию которую вы хотите вычислить( g, f, y): "))
if (fun == 'g'):
    g = (-1 * (2 * (-5 * a**2 + 3 * a * x + 2 * x**2) / (5 * a**2 + 9 * a * x - 2 * x**2)))
    print(g)
elif (fun == 'f'):
    f = (sin(pi * (10 * a**2 + 37 * a * x + 7 * x**2)))
    print(f)
elif (fun == 'y'):
    y = (log(-5 * a**2 - 16 * a * x + 16 * x**2 + 1) / log(2))
    print(y)
else:
    print("ERROR")
