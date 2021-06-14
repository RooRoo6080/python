def words_with_duplicate_letters(s):
    ans = []
    l = s.split(", ")
    for i in l:
        for j in i:
            count = i.count(j)
            if count > 1:
                ans.append(i)
                break
    if ans != []:
        return False
    else:
        return True


string = raw_input("Enter a sentence | ex: Look before you leap")
print words_with_duplicate_letters(string)