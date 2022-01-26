#해결 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/7576
[7576] : 토마토
"""

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 0:
                q.append((ny, nx))
                arr[ny][nx] = arr[y][x] + 1
bfs()
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
        answer = max(answer, arr[i][j])

print(answer-1)

