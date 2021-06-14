a = raw_input()
b = a.split(", ")
for i in range(0,len(b)):
    for j in b[i]:
        if j == "7":
            print "Boom!"
            exit()
print "there is no 7 in the list"
