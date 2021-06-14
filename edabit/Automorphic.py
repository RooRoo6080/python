a = int(raw_input())
b = str(a ** 2)
print b
c = len(b) - 1
print c
print b[c]
if str(a) == b[c]:
    print "True"
else:
    print 'False'
