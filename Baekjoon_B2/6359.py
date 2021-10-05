import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    lst = [0 for _ in range(n)]
    for j in range(1, n+1):
        for k in range(j, n+1, j):
            lst[k-1] += 1

    cnt = 0
    for i in lst:
        if i % 2 == 1: cnt += 1
    print(cnt)