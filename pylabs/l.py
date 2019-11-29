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


def gfunc():
    g = (-1 * (2 * (-5 * a ** 2 + 3 * a * x + 2 * x ** 2) / (5 * a ** 2 + 9 * a * x - 2 * x ** 2)))
    return g


while True:
    while p >= 0:
        if p == 0:
            quiestion = input('Вы хотите продолжить?(yes, no)')
            if quiestion == 'yes':
                p = int(input('Сколько счтитать?'))
                sh = float(input('С каким шагом?: '))
            else:
                print('END')
