a = raw_input()
a = a.split(", ")
b = raw_input()
b = b.split(", ")
c = []
d = []
e = ["0"]
for i in b:
    m = int(i)
    for j in range(1, m):
        c.append("0")
        d.append("1")
    if str(c) in a:
        a.replace(c, d)
for n in a:
    e.append('0')
    if e in a:
        print False
        exit()
print True
