from math import *

a = float(input("Введите a: "))
x = float(input("Введите x: "))
fun = str(input("Введите ф-ию которую вы хотите вычислить( g, f, y): "))
p = int(input('Сколько считать: '))
sh = float(input('С каким шагом?: '))

mf = []
mg = []
my = []

mg_max = 0
mf_max = 0
my_max = 0

while p >= 0:
    if p == 0:
        question = input("Вы хотите продолжить?(да, нет)")
        if question == 'да':
            p = int(input('Сколько счтитать?'))
            sh = float(input('С каким шагом?: '))
        else:
            print('END')

    if fun == 'g':
        for i in range(p):
            g = (-1 * (2 * (-5 * a ** 2 + 3 * a * x + 2 * x ** 2) / (5 * a ** 2 + 9 * a * x - 2 * x ** 2)))
            if (5 * a ** 2 + 9 * a * x - 2 * x ** 2) == 0:
                print('ERROR')
            else:
                if g > mg_max:
                    mg_max = g
                mg.append(g)
                a += sh

    elif fun == 'f':
        for i in range(p):
            f = (sin(pi * (10 * a ** 2 + 37 * a * x + 7 * x ** 2)))
            if a == 0:
                print('ERROR')
            else:
                if f > mf_max:
                    mf_max = f
                    mf.append(f)
                a += sh

    elif fun == 'y':
        for i in range(p):
            y = (log(-5 * a ** 2 - 16 * a * x + 16 * x ** 2 + 1) / log(2))
            print(y)
            a += sh
        if log(2) == 0:
            print("ERROR")
        else:
            if y > my_max:
                my_max = y
                my.append(y)
            a += sh
    else:
        print("ERROR")
    p -= 1

    print('Максимальный эл-т массива mg: ' + str(mg_max))
    print('Максимальный эл-т массива mf: ' + str(mf_max))
    print('Максимальный эл-т массива my: ' + str(my_max))
    print()
    print(mg)
    print(mf)
    print(my)

