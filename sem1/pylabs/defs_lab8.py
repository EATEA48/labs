import random


def random_x_y(N):
    xy = []

    for i in range(N):
        xy.append((random.uniform(-5, 5), random.uniform(-5, 5)))

    return xy
