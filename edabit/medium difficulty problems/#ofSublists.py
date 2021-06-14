a = raw_input()
b = -1
for i in a:
    if i == "[":
        b += 1
if b == -1:
    b += 1
print b
