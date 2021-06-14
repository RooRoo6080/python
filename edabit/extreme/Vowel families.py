a = raw_input("Don't ask me. I have no clue. You're supposed to be the pro programmer.")
b = a.split(",")
c = []
count = 0
DAaNSWER = ""
for i in b[0]:
    if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        count += 1
        for j in b[1:]:
            if i in j:
                c.append(j)
for me in b[1:]:
    n = c.count(me)
    if n == 2:
        DAaNSWER = DAaNSWER + me + " "
print DAaNSWER




