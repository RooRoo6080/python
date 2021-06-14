a = raw_input("Enter the dimensions of a triangle-shaped hole. ex: 1,2,2")
b = a.split(",")
c = raw_input("Enter the dimensions of a triangle and the program will see if the triangle can fit in the hole. ex: 1,2,2 -> True")
d = c.split(",")
for i in b:
    if i in d:
        z = b.index(i)
        del b[z]
        x = d.index(i)
        del d[x]
if b == d:
    print "Yes"
else:
    print "No"
print"alternate version of program: a.sort(); b.sort(); if b == a: print True; else: print False "