a = int(raw_input("intersecting number"))
count = 0
huh = 0
while huh <= 2:
    b = raw_input("pair")
    sb = b.split(",")
    if a > int(sb[0]) and a < int(sb[1]):
        count += 1
    huh += 1
print count