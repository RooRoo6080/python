a = raw_input("Enter a bunch of numbers")
b = a.split(" ")
c = 0
for i in range(0, len(b)):
    v = int(b[i])
    c += v
m = c / len(b)
print m