# https://www.acmicpc.net/problem/1707

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, flag):
    global answer
    visited[start] = flag
    for adj in graph[start]:
        if visited[adj] == flag:
            answer = 0
            break

        if not visited[adj]:
            dfs(adj, -flag)


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for __ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    answer = 1
    for i in range(1, V+1):
        if not visited[i]:
            dfs(i, 1)

        if answer == 0:
            print("NO")
            break
    else:
        print("YES")