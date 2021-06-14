def larger_than_all_numbers_to_their_right(list):
    ans = []
    for i in list:
        for j in list[i.index() + 1:]:
            if i <= j:
                break
        ans.append(i)
    return ans

