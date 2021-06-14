a = int(raw_input("enter what 'bonacci' number you want. ex: 3 -> next number is the sum of the 3 numbers before it."))
b = int(raw_input("Enter the index of the number you want ex: 10 -> returns 10th number of 3-bonacci"))
c = []
for i in range(0, a - 1):
    c.append(0)
c.append(1)
while len(c) < b:
    ind = len(c) - 1
    d = 0
    for j in range(0, a):
        d += c[ind]
        ind -= 1
    c.append(d)
print c
print c[b - 1]