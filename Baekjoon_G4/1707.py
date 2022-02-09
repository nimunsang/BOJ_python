#해결 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/1707
[1707] : 이분 그래프
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(start, mask):
        visited[start] = mask
        for vertex in graph[start]:
            if visited[vertex] == 0:
                if not dfs(vertex, -mask):
                    return False
            elif visited[vertex] == visited[start]:
                return False
        
        return True
    
    for i in range(1, V+1):
        if visited[i] == 0:
            if not dfs(i, 1):
                print("NO")
                break
    else:
        print("YES")