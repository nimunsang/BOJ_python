lst = list(map(int, input().split()))

lst.sort()

s = input()
for i in range(3):
    if s[i] == 'A': print(lst[0], end = " ")
    if s[i] == 'B': print(lst[1], end = " ")
    if s[i] == 'C': print(lst[2], end = " ")