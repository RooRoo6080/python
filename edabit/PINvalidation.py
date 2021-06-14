pin = raw_input()
if len(pin) == 4 or len(pin) == 6:
    for i in pin:
        if i.isalpha():
            print "False"
            exit()
        else:
            continue
else:
    print "False"
    exit()
print "True"
