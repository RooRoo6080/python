num = int(raw_input("Enter a number"))
x = 1
y = 2
z = 0
while y <= num:
    z = x + y
    x = y
    y = z
    if y == num:
        print "Your number is a Fibbinocci number"
        break
    elif y > num:
        print"Your number is not a fibbinocci number"