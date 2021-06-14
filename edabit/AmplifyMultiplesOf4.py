num = int(raw_input())
l = []
for i in range(1, num + 1):
    if i % 4 == 0:
        i = i * 10
    l.append(i)
print l
