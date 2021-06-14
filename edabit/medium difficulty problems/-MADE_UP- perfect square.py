import math
a = int(raw_input())
for i in range(1,a):
    if math.sqrt(a) == i:
        print "Yes"
        exit()
print "No"