a = raw_input()
b = raw_input()
c = 0
d = []
for i in a:
    if i == b:
        d.append(c)
    c += 1
while len(d) > 2:
    d.pop(1)
if len(d) == 1:
    d.append(d[0])
print d
