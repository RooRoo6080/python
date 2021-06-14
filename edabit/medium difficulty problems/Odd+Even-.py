huh = raw_input("list")
a = huh.split(" ")
b = int(raw_input())
l = []
for i in range(1, b + 1):
    for k in a:
        j = int(k)
        if j % 2 == 0:
            j -= 2
        else:
            j += 2
    l.append(j)
print l
