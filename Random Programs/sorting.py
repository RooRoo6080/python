s = raw_input("Enter stuff to alphabetically sort")
b = ""
v = s.split(" ")
v.sort()
for i in range(0,len(v)):
    b = b + v[i] + " "
print b
