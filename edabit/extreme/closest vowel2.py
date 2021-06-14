a = raw_input()
b = []
newList = []
length =0
shortLen =1
index = 1
ind = 0
iind = 1
x = 0
for i in a:
    if i in ["a", "e", "i", "o", "u"]:
        b.append(0)
    else:
        b.append(i)
        length+=1
print b
for j in b:
    if j != 0:
        if shortLen <= length/2:
            newList.append(index)
            index = index +1
            shortLen = shortLen +1
        else:
            newList.append(4)
    else:
        newList.append(0)
print newList

for i in xrange(len(newList)):
      if newList[i] == 4:
          x = length / 2
          if length%2 == 0:
            newList[i] = x
            x -= 1
          else :
            newList[i] = x -1
            x -= 1

print newList