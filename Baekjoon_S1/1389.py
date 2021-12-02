#30분 #그래프이론 #그래프탐색 #BFS #플로이드-와샬
"""
https://www.acmicpc.net/problem/1389
[1389] : 케빈 베이컨의 6단계 법칙
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


graph = [[] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i] = list(set(graph[i]))

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

anslist = []
for i in range(1, N+1):
    visited = [0] * (N+1)
    bfs(i)
    ans = sum(visited) - N
    anslist.append([i, ans])

anslist.sort(key = lambda x: (x[1], x[0]))
print(anslist[0][0])