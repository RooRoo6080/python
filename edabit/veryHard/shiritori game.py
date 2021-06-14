b = raw_input()
a = b.split(", ")
c = []
for i in a[2:]:
    if i in c:
        print "invalid"
        exit()
    n = len(c)
    for j in c[n - 1]:
        if j != i[0]:
            print "invalid"
            exit()
print "valid"
