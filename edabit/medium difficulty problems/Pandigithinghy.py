a = raw_input()
for i in range(1,10):
    if str(i) not in a:
        print "False"
        exit()
print "True"