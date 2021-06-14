a = raw_input()
b = []
for i in a:
    i = int(i)
    b.append(i)
b.sort()
b.remove(b[0])
print b
