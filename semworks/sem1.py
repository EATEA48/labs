
a = float(input("Введите число из которого нужно извлечь корень: "))
x = 3
b = 0

while b != (a ** 0.5):
    b = 0.5 * (x + a/x )
    x = b
print(int(b))

