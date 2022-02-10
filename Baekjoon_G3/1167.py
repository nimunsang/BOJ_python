#해결 #그래프이론 #그래프탐색 #트리 #DFS
"""
https://www.acmicpc.net/problem/1167
[1167] : 트리의 지름
"""

import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    a = list(map(int, input().split()))
    s = a[0]
    i = 1
    while a[i] != -1:
        graph[s].append((a[i], a[i+1]))
        i += 2


def dfs(v, weight):
    global res, maxnode
    visited[v] = 1

    for next_v, distance in graph[v]:
        visit = 0
        if not visited[next_v]:
            visited[next_v] = 1
            visit = 1
            dfs(next_v, weight + distance)
            visited[next_v] = 0
    if visit == 0:
        if weight > res:
            res = weight
            maxnode = v

visited = [0] * (V+1)
maxnode = 1

res = 0
dfs(1, 0)
visited[1] = 0

res = 0
dfs(maxnode, 0)
print(res)