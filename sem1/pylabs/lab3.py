import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='f', help='Simple value')
parser.add_argument('-a', action='store', dest='a', help='Simple value')
parser.add_argument('-x', action='store', dest='x', help='Simple value')
args = parser.parse_args()

#a = float(input("Введите a: "))
#x = float(input("Введите x: "))
#fun = str(input("Введите ф-ию которую вы хотите вычислить( g, f, y): "))
fun = float(args.f)
a = float(args.a)
x = float(args.x)
print(fun, a, x)
f = (math.sin(math.pi * (10 * a**2 + 37 * a * x + 7 * x**2)))
print(f)

g = (-1 * (2 * (-5 * a**2 + 3 * a * x + 2 * x**2) /(-5 * a**2 + 9*a*x - 2*x**2)))
print(g)

y = (math.log(-5 * a**2 - 16 * a * x + 16 * x**2 + 1) / math.log(2))
print(y) 
if (fun == 'g'):
    znam = (-5 * a**2 + 9*a*x - 2*x**2)
    if (znam != 0):
        g = (-1 * (2 * (-5 * a**2 + 3 * a * x + 2 * x**2) /(znam)))
        print(g)
elif (fun == 'f'):
    f = (sin(pi * (10 * a**2 + 37 * a * x + 7 * x**2)))
    answer = args.f
    print(answer)
elif (fun == 'y'):
    y = (math.log(-5 * a**2 - 16 * a * x + 16 * x**2 + 1) / math.log(2))
    print(y)
else:
    print(" ")


