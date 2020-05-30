import time
import random
import math
begin = time.process_time()
def coordinates(kol):
    data = []
    for i in range(kol):
        x = random.uniform(0, 500)
        y = random.uniform(0, 500)
        data.append((x,y))
    return(data)

def centre(dots):
    c = random.choice(dots)
    return(c)

def kollvo(tochki, centr, radius):
    count = 0
    for i in tochki:
        a = i
        if math.pow(a[0] - centr[0], 2) - math.pow(a[1] - centr[1], 2) <= math.pow(radius, 2):
            count+=1
    return(count)

while True:
    try:
        r = float(input('Введи радиус: '))
        point = int(input('Введи кол-во точек: '))
        break
    except:
        print('Попробуй еще разок')
points = coordinates(point)
print('Список точек: ', points)
mid = centre(points)
print()
print('Центр окружности: ', mid)
print()
ans = kollvo(points, mid, r)
if ans == 0:
    print('В данную область точки не входят')
else:
    print('Точек, входящих в окружность: ', ans)

time = (time.process_time() - begin)
file = open('time.txt', 'a')
file.write(str(time) + '\n')
file.close()


