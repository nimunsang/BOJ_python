#해결 #그래프이론 #최소 스패닝 트리
"""
https://www.acmicpc.net/problem/1197
[1197] : 최소 스패닝 트리
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

V, E = map(int, input().split())
Elist = [list(map(int, input().split())) for _ in range(E)]
Elist.sort(key = lambda x: x[2])
root = [i for i in range(V+1)]

answer = 0
for A, B, C in Elist:

    if find(A) == find(B):
        continue

    union(A, B)
    answer += C

print(answer)