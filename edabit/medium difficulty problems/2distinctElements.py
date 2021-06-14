a = raw_input()
b = a.split(", ")
c = sorted(set(b), key=b.index)
d = []
for i in c:
    n = a.count(i)
    if n == 1:
        d.append(i)
print d
