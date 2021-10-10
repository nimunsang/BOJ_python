s = input().upper()

list_s = list(set(s))
count_s = [0 for _ in range(len(list_s))]

for i in range(len(list_s)):
    count_s[i] += s.count(list_s[i])

if count_s.count(max(count_s)) > 1: print("?")
else: print(list_s[count_s.index(max(count_s))])