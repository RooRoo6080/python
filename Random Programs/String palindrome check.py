x = raw_input("enter numbers or letters")
z = x.count("") - 1
if z % 2 == 0:
    c = z / 2
    b = x[:c]
    v = b[::-1]
    if v == x[c:]:
        print x, "is a palindrome."
    else:
        print x, "is NOT a palindrome"
else:
    c = (z - 1) / 2
    b = x[:c]
    v = b[::-1]
    l = c + 1
    if v == x[l:]:
        print x, "is a palindrome."
    else:
        print x, "is NOT a palindrome"

