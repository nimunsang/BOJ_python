import sys
input = sys.stdin.readline

lst = []
for i in range(9):
    lst.append(int(input()))

tmp = sum(lst) - 100

lst.sort()
for i in range(8):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == tmp:
            break
    if lst[i] + lst[j] == tmp: 
        lst.remove(lst[i])
        lst.remove(lst[j-1])
        break

for i in lst:
    print(i)