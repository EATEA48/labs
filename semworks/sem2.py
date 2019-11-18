a = int(input())
b = int(input())

for i in range(a, b):
    min = i + 1
    if i < min:
        min = i
print(min)