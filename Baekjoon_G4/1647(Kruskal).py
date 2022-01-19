#10분 #그래프이론 #최소스패닝트리
"""
https://www.acmicpc.net/problem/1647
[1647] : 도시 분할 계획
"""

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rootx = root[x]
    rooty = root[y]
    if rootx > rooty:
        root[rootx] = rooty
    else:
        root[rooty] = rootx

N, M = map(int, input().split())
Elist = [list(map(int, input().split())) for _ in range(M)]
Elist.sort(key = lambda x: x[2])
root = [i for i in range(N+1)]

answer = 0
maximum = 0
for A, B, C in Elist:
    roota = find(A)
    rootb = find(B)
    if roota == rootb:
        continue

    union(A, B)
    answer += C
    maximum = max(maximum, C)

print(answer- maximum)