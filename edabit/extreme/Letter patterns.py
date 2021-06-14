a = raw_input("enter a string ex:ABAB")
b = raw_input("enter another string. This program will tell you if the letter patterns are the same. ex: CDCD -> True (ABAB has the same pattern as CDCD)")
c = sorted(set(a), key=a.index)
d = sorted(set(b), key=b.index)
count = "1"
count1 = "1"
print c
print d
for i in c:
    a = a.replace(i, count)
    count = int(count)
    count += 1
    count = str(count)
for j in d:
    b = b.replace(j, count1)
    count1 = int(count1)
    count1 += 1
    count1 = str(count1)
if a == b:
    print True
else:
    print False
