#2시간 #구현 #그래프이론 #그래프탐색 #BFS #시뮬레이션
"""
https://www.acmicpc.net/problem/16236
[16236] : 아기 상어
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
scale = 2
sx, sy = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sy, sx = i, j

def bfs(sy, sx, scale):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 0
    arr[sy][sx] = 0
    eat = []
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == -1 and arr[ny][nx] <= scale:
                if 0 < arr[ny][nx] < scale:
                    visited[ny][nx] = visited[y][x] + 1
                    eat.append((ny, nx, visited[ny][nx]))
                
                else:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
    return eat

time = 0
eat_count = 0
while True:
    visited = [[-1] * N for _ in range(N)]
    eat = bfs(sy, sx, scale)
    if len(eat) == 0:
        print(time)
        break

    eat.sort(key = lambda x: (x[2], x[0], x[1]))
    sy, sx = eat[0][0], eat[0][1]
    time += visited[sy][sx]
    eat_count += 1
    if scale == eat_count:
        scale += 1
        eat_count = 0
