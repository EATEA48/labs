from random import randint

array = []
N = 30
k = 0
z = 0

for i in range(N):
    array.append(randint(1, 99))
    print(array[i], end=" ")
for i in range(N - 1):
    for j in range(N - 1 - i):
        if array[j] > array[j + 1]:
           array[j], array[j+1] = array[j+1], array[j]
print()
for i in range(N):
    print(array[i], end= " ")
for i in range(5):
    k += array[i]
print()
print(k)
for i in range (25,N):
    z += array[i]
print()
print(z)

