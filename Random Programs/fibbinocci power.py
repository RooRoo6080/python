num = int(raw_input("Enter a number"))
x = 0
y = 1
output = 1
print 0
while y <= num:
    print output
    output = x + y
    x = y
    y = output