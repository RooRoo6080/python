a = raw_input()
b = a.split(" ")
if b[0] == b[1] and b[0] == b[2]:
    print "3"
elif b[0] == b[1] or b[0] == b[2]:
    print "2"
else:
    print "0"
