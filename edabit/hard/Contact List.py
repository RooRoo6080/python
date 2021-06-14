def contact_list(l, alphabetichoose):
    ans = ""
    newlist = []
    for i in l:
        k = i.split(" ")
        n = k[::-1]
        " ".join(n)
        newlist.append(n)
    if alphabetichoose == "ASC":
        a = sorted(newlist)
    else:
        a = sorted(newlist, reverse=True)
    for t in a:
        g = t[::-1]
        h = " ".join(g)
        ans = ans + h + ", "
    return ans


v = raw_input("Enter a list of names.")
yello = v.split(", ")
x = raw_input("Enter 'ASC' or 'DESC'")
print contact_list(yello, x)
