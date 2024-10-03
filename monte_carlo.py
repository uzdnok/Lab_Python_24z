import random
import math


def montecarlo(n, k):
    trafy = 0
    strzaly = n * k
    for i in range(n):
        for j in range(k):
            x = random.random()
            y = random.random()
            if x*x + y*y <= 1:
                trafy += 1
    return trafy / strzaly


n = input()
k = input()
montecarlo(n, k)
