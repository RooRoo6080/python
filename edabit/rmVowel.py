a = raw_input()
b = ""
for i in a:
    if i not in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
        b += i
print b
