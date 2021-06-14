a = raw_input()
b = raw_input()
d = []
for i in range(0, len(a) - 1):
    if a[i] in b:
        c = b.index(a[i])
        d.append(c)
    else:
        print False
        exit()
for j in range(0,len(d) - 1):
    if d[j] > d[j + 1]:
        print False
        exit()
print True
