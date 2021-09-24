import sys

lst = []
for i in range(9):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)

max = 0
index1 = 0
index2 = 0
for i in lst:
    cnt = 0
    for j in i:
        cnt += 1
        if j > max: 
            max = j
            index1 = lst.index(i)
            index2 = cnt
 

print(max)
print("{0} {1}".format(index1+1, index2))






