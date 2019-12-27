xa =[]
ya = []

x = [int(i) for i in input('Введите координаты х: ').split()]
y = [int(i) for i in input('Введите координаты y: ').split()]

a = float(input('Введите скаляр а: '))

for elem_x in x:
    xa.append(elem_x * a)
print('Вектор х, умноженный на скаляр: ', xa)

for elem in zip(y, xa):
    x_elem, y_elem = elem
    ya.append(x_elem + y_elem)

print('Вектор у: ', ya)