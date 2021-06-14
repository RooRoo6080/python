string = raw_input()
ls = string.split(",")
s = set(ls)
ans = ""
for i in s:
    if ls.count(i) % 2 == 1:
        ans = ans + i + " "
print ans
