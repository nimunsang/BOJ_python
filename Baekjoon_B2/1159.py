import sys
input = sys.stdin.readline

N = int(input())

lst = [input()[0] for _ in range(N)]

new_lst = []
for i in lst:
    if lst.count(i) >= 5:
        new_lst.append(i)

if len(new_lst) == 0: print("PREDAJA")
else:
    new_lst = list(set(new_lst))
    new_lst.sort()
    s = ""
    for i in new_lst:
        s += i
    print(s)
