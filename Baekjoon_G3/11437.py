#다시 #트리 #최소공통조상
"""
https://www.acmicpc.net/problem/11437
[11437] : LCA
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for adj in graph[x]:
        if visited[adj]:
            continue

        parent[adj] = x
        dfs(adj, depth+1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

N = int(input())
graph = [[] for _ in range(N+1)]
d = [0] * (N+1)
visited = [0] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))