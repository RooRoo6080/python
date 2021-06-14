a = raw_input()
sum = 0
for i in a:
    jalopy = int(i)
    sum += jalopy
if sum % 2 == 0:
    print "Evenish"
else:
    print "Oddish"