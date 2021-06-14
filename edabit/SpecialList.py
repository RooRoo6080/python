a = raw_input()
a = a.split(", ")
b = 0
for i in a:
    i = int(i)
    if b % 2 == 0:
        if i % 2 != 0:
            print "False"
            exit()
    elif b % 2 == 1:
        if i % 2 == 0:
            print "False"
            exit()
    b += 1
print "True"
