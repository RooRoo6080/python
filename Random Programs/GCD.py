a = int(raw_input())
b = int(raw_input())
c = a
while c > 0:
    if b % c == 0:
        if a % c == 0:
            print c, "is the GCD of", a, "and", b
            exit()
    c -= 1
