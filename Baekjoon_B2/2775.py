import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    lst = []
    new_lst = []
    for i in range(1, n+1):
        new_lst.append(i)
    lst.append(new_lst)

    for i in range(k):
        new_lst = []
        s = 0
        for j in range(n):
            s += lst[i][j]
            new_lst.append(s)
        lst.append(new_lst)
    print(lst[k][n-1])