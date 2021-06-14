def numbers_in_strings(l):
    ans = []
    for i in l:
        for j in i:
            if j in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                ans.append(i)
            break
    return ans


ls = raw_input("Enter a list of numbers and letters | ex: 1a, a, 2b, b").split(", ")
print numbers_in_strings(ls)