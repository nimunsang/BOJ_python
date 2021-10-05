lst = []
for i in range(9):
    lst.append(int(input()))

mask = sum(lst) - 100

for i in range(8):
    for j in range(i+1, 9):
        if lst[i]+lst[j] == mask:
            lst.remove(lst[i])
            lst.remove(lst[j-1])
            break
    if len(lst) == 7: break

for i in lst:
    print(i)