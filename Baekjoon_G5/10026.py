#30분 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/10026
[10026] : 적록색약
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mask = ['R', 'G']

def bfs(y, x, disease):
    color = arr[y][x]
    q = deque([])
    q.append([y, x])
    visited[y][x] = 1
    while q:
        v = q.popleft()
        for i in range(4):
            a = v[0] + dy[i]
            b = v[1] + dx[i]

            if 0<=a<N and 0<=b<N and visited[a][b] == 0:
                if disease == True:
                    if arr[a][b] == color or\
                        (arr[a][b] in mask and color in mask):
                        q.append([a, b])
                        visited[a][b] = 1
                else:
                    if arr[a][b] == color:
                        q.append([a, b])
                        visited[a][b] = 1

ans = [0, 0]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            ans[0] += 1
            bfs(i, j, False)

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            ans[1] += 1
            bfs(i, j, True)

print(*ans)