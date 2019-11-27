import random
a = float(input())
x = float(random.randint(0, 9))
i = 0
while abs(x-a) > 0.001:
    answer = 0.5 * (x + a/x)
    x = answer
    i += 1
    if i == 10:
        print(answer)
