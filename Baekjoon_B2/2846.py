N = int(input())
s = list(map(int, input().split()))

lst = []
new_lst = []
i = 0

while True:
    lst.append(s[i])
    i += 1

    if s[i-1] >= s[i]:
        new_lst.append(lst)
        lst = []

    if i == N-1:
        lst.append(s[i])
        new_lst.append(lst)
        break

if len(new_lst) == N: print(0)
else:
    res = 0
    for i in new_lst:        
        if (max(i) - min(i)) > res:
            res = max(i) - min(i)
    print(res)