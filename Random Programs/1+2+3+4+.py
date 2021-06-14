start = int(raw_input(""))
end = int(raw_input(""))
hm = int(raw_input(""))
ans = 0
for i in range(start, end + 1, hm):
    ans += i
print ans
