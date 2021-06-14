s1 = raw_input("")
s2 = raw_input("")
what = ""
count = 0
for i in s1:
    for j in s2:
        if i == j:
            count += 1
            j += " "
            what += j
            break
print count, "(", what, ")"
