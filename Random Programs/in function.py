"""string = raw_input()
sub = raw_input()
lenSub = len(sub)
d = 0
while lenSub <= len(string):
    if string[d:lenSub] == sub:
        print sub, "is in", string
        exit()
    d += 1
    lenSub += 1
print sub, "is not in", string
"""