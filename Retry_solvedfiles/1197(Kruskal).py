# https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)] 
arr.sort(key = lambda x: x[2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[a] = b

parent = [i for i in range(V+1)]
graph = [[] for _ in range(V+1)]
result = 0
for a, b, c in arr:
    if find(a) == find(b):
        continue

    union(a, b)
    result += c

print(result)