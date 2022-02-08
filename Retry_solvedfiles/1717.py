# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b

for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")