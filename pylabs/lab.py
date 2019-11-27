
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
    # Проверка на кол-во счетчика
    if p == 0:
        question = input("Вы хотите продолжить?(да, нет)")
        # Проверка на продолжение программы
        if question == 'да':
            p = int(input('Сколько счтитать?'))
            sh = float(input('С каким шагом?: '))
        else:
            print('END')
    # Проверка на ограничения
    if a != 0 and a != x:
        # Ф-ия g
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
        # Ф-ия f
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
        # Ф-ия y
        elif fun == 'y':
            for i in range(p):
                y = (log(-5 * a ** 2 - 16 * a * x + 16 * x ** 2 + 1) /log(2))
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
    # Проверка на окончание цикла
    if p == 0:
        output = str(input('Как вывести ответ? (tab, str)'))
        if output == 'str':
            # Вывод выбранной ф-ии и ее max э-та
            if fun == 'g':
                print('Максимальный эл-т массива mg: ' + str(mg_max))
                # Вывод массива в строку
                print(str(mg))
            if fun == 'f':
                print('Максимальный эл-т массива mf: ' + str(mf_max))
                # Вывод массива в строку
                print(mf)
            if fun == 'y':
                print('Максимальный эл-т массива my: ' + str(my_max))
                # Вывод массива в строку
                print(my)
        elif output == 'tab':
            if fun == 'g':
                for i in mg:
                    mg_i = i
                    print('| ' + 'a= ' + str(a) + ' | ' + ' x= ' + str(x) + ' | ' + str(mg_i) + ' |')
                    i += 1
            if fun == 'f':
                for i in mf:
                    mf_i = i
                    print('| ' + 'a= ' + str(a) + ' | ' + ' x= ' + str(x) + ' | ' + str(mf_i) + ' |')
                    i += 1
            if fun == 'y':
                for i in my:
                    my_i = i
                    print('| ' + 'a= ' + str(a) + ' | ' + ' x= ' + str(x) + ' | ' + str(my_i) + ' |')
                    i += 1

my_file_mg = open('mg_list.txt', 'w')
for i in mg:
    my_file_mg.write(str(i) + '\n')
my_file_mg.close
my_file_mf = open('mf_list.txt', 'w')
my_file_mf.write(str(mf) + '\n')
my_file_mf.close()
my_file_my = open('my_list.txt', 'w')
my_file_my.write(str(my) + '\n')
my_file_my.close()

mf.clear()
mg.clear()
my.clear()


my_file_mg = open('mg_list.txt', 'r')
mg = [float(e.strip()) for e in my_file_mg.readlines()]
my_file_mg.close()
print(mg)

my_file_mf = open('mf_list.txt', 'r')
mf = [float(e.strip()) for e in my_file_mf.readlines()]
my_file_mf.close()
print(mf)

my_file_my = open('my_list.txt' , 'r')
m = [float(e.strip()) for e in my_file_my.readlines()]
my_file_my.close()
print(my)