a = raw_input()
b = a.split(" ")
c = set(b)
d = []
for i in c:
    d += i
e = d.sort()
if len(d) % 2 == 0:
    z = len(d) / 2
    x = len(d) / 2 + 1
    y = float((d[z] + d[x])) / 2
    print y
else:
    v = (len(d) + 1) / 2
    print d[v]


