x = raw_input("Enter a number-")
f = 0
for i in x:
    i = int(i)
    z = i * i * i
    f = f + z
g = str(f)
if g == x:
    print x , "is an armstrong number"
else:
    print x, "is not an armstrong number"