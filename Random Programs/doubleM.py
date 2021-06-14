a = raw_input("list numbers. gives mean and medium")
a.split(", ")
b = len(a)
c = 0
for i in a:
    int(i)
    c += i
print "mean ->", c / b
a.sort()
if b % 2 == 0:
    c = (int(a[b/2]) + int(a[b/2+1])) / 2
else:
    c = int(a[b/2 + 0.5])
print "medium ->", c
