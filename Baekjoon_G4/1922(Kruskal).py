#해결 #그래프이론 #최소스패닝트리
"""
https://www.acmicpc.net/problem/1922
[1922] : 네트워크 연결
"""

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    
    return root[x]

def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx > rooty:
        root[rootx] = rooty
    else:
        root[rooty] = rootx


N = int(input())
M = int(input())
root = [i for i in range(N+1)]
Elist = [list(map(int, input().split())) for _ in range(M)]
Elist.sort(key = lambda x: x[2])

answer = 0
for a, b, c in Elist:
    if find(a) == find(b):
        continue

    answer += c
    union(a, b)
print(answer)