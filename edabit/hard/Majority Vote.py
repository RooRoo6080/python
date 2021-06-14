def majority_vote(list):
    majorities = []
    for i in set(list):
        if list.count(i) > len(list) / 2:
            majorities.append(i)
    if len(majorities) != 1:
        return "None"
    else:
        return majorities


a = raw_input("Enter a list | ex: A, A, A, B, C, A")
a.split(", ")
print majority_vote(a)

