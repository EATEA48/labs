from math import *

a = float(input())
x = float(input())

g = -1 * (2 * (-5 * a**2 + 3 * a * x + 2 * x**2) / (5 * a**2 + 9 * a * x - 2 * x**2))

f = (sin(pi * (10 * a**2 + 37 * a * x + 7 * x**2)))

y = (log(-5 * a**2 - 16 * a * x + 16 * x**2 + 1) / log(2))

print(g)
print(f)
print(y)