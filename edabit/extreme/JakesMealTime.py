a = raw_input("Jake eats at 7 am, 12 pm, and 7 pm. Enter a time and the program will return in how many hours and minutes Jack will eat. ex: 5:50 a.m. -> 1,10 (first hour then minutes)")
a = a.split(" ")
b = a[0].split(":")
c = int(b[0])
d = []
if b[1] != "00":
    d.append(60 - int(b[1]))
    b[1] = "00"
    c += 1
if a[1] == "a.m.":
    if c < 7:
        d.insert(0, 7 - c)
    else:
        d.insert(0, 12 - c)
else:
    if c < 7:
        d.insert(0, 7 - c)
    else:
        d.insert(0, 7 - c)
if len(d) == 1:
    d.append(0)
print d
