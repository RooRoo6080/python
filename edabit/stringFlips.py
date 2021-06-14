a = raw_input()
b = raw_input("Enter 'word' or 'sentence'")
if b == "word":
    c = []
    d = ""
    for i in a:
        c.insert(0, i)
    for j in c:
        d = d + j
    print d
elif b == "sentence":
    c = a.split(" ")
    d = ""
    for i in c:
        d = i + " " + d
    print d
else:
    print "  _    _  "
    print "  |    |  "
    print "  ______  "
    print " /      \ "