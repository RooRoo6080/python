def uppercaseChar(s):
    splitS = list(s)
    count = 0
    ans = ""
    for i in splitS:
        count += 1
        if i.isupper() == True:
            ans = ans + str(count) + ","
    return ans


hmm = raw_input()
print uppercaseChar(hmm)



q