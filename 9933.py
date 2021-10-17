N = int(input())

lst = []
for i in range(N):
    lst.append(input())

for i in lst:
    if i[::-1] in lst:
        print(len(i), i[len(i)//2])
        break