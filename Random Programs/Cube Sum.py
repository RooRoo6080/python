choose = raw_input("Do you want to square it, cube it, or something else. You can enter square, cube, or any number you want to exponent it by.")
if choose == "Square" or choose == "square":
    z = 2
elif choose == "Cube" or choose == "cube":
    z = 3
else:
    z = int(choose)
num = int(raw_input("enter a number"))
x = 0
for i in range(1, num + 1):
    i = i ** z
    x += i
print x
