s = int(input())

lst = []
for i in range(9):
    a = int(input())
    lst.append(a)

print(s - sum(lst))