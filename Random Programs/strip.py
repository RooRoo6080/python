def strip(string):
    stripped = ""
    string = str(string)
    li = list(string)
    for i in li:
        if i != " ":
            stripped += i
    return stripped
