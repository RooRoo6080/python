def first_before_second_letter(string, l1, l2):
    index = 0
    list(string)
    for i in string:
        if i == l2:
            for j in string[index:]:
                if j == l1:
                    return False
                    exit()
        index += 1
    return True


a = raw_input("Enter a string | ex: a rabbit jumps joyfully")
b = raw_input("Enter a letter | ex: a")
c = raw_input("Enter a letter | ex: j")
print first_before_second_letter(a, b, c)