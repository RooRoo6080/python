s = raw_input("enter a sentence")
i = raw_input("enter a letter that you want to take away from the sentence.")
if len(i) != 1:
    print "ONE LETTER! Not", len(i), "! It says A letter."
    exit()
v = ""
for j in s:
    if i == j:
        j = ""
    v = v + j
print v