a = raw_input("input a string and the program will show how far away the closest vowel is from each letter in the string. ex: abbb -> 0,1,2,3:: PROGRAM NOT WORKING")
b = list(a)
c = []
fv = 0
bv = 0
ind = 0
iind = 0
for i in b:
    if i in ["a", "e", "i", "o", "u"]:
        c.append(0)
    else:
        for j in b[ind:]:
            if j not in ["a", "e", "i", "o", "u"]:
                fv = iind
            iind += 1
        for k in b[:ind]:
            if k not in ["a", "e", "i", "o", "u"]:
                bv = iind
            iind += 1
        if fv < bv:
            c.append(fv)
        else:
            c.append(bv)
    ind += 1
    iind += 1
print c
