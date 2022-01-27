#해결 #그래프이론 #DFS #BFS
"""
https://www.acmicpc.net/problem/11724
[11724] : 연결 요소의 개수
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        for i in range(1, N+1):
            if graph[i][v] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)