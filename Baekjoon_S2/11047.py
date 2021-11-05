#10분 #그리디알고리즘
"""
https://www.acmicpc.net/problem/11047
[11047] : 동전 0
"""

N, K = map(int, input().split())

lst = []
for i in range(N):
    lst.append(int(input()))

cnt = 0
for i in range(N-1, -1, -1):
    while K >= lst[i]:
        cnt += K//lst[i]
        K %= lst[i]
    if K == 0:
        print(cnt)
        break