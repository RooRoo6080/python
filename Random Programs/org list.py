import random
ans = ""
l = []
k = []
j = []
for i in range(1, 11):
    z = random.randint(1, 100)
    l.append(z)
for v in l:
    if v % 2 == 0:
        j.append(v)
    else:
        k.append(v)
j.sort()
k.sort()
o = k + j
for h in o:
    h = str(h)
    ans = ans + h + ","
ans = ans[:-1]
print ans
