def indexAll(list, input):
    r = []
    count = 0
    for i in list:
        if input == i:
            r.append(count)
        count += 1
    return r
