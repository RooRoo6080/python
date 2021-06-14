l = ['1', '1', '2', '-2', '5', '2', '4', '4', '-1', '-2', '5']

ans = ""
for i in l:
    print l
    ans += i
    for j in l:
        if j == i:
            l.remove(i)
print ans
