import random
import math
L = []
w = random.randint(0, 9)
for k in range(1, 10):
    a = []
    number_change = 0
    x = random.randint(10, 100)
    y = random.uniform(-10, -100)
    code = str(math.sqrt(x) * x + x * y - math.sqrt(x - y))
    for i in code:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            a.append(i)
    for j in a:
        number_change += int(j)
    L.append(number_change)
L.sort()
final = L[1] + L[w] - 5
print final
