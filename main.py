import random
import math




def montecarlo(n, k):
   trafy = 0
   for i in range(n):
       for j in range(k):
           x = random.random()
           y = random.random()
           if x * x + y * y <= 1:
               trafy += 1
       if i == n - 1:
           print("Uzyskane przybliżenie: ")
       print(4 * (trafy / (k * (i + 1))))




n = input()
k = input()
n = int(n)
k = int(k)
montecarlo(n, k)


print("Dokładna wartość Pi: ")
print(math.pi)
