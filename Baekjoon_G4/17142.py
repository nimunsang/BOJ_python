#1시간 #그래프이론 #브루트포스알고리즘 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/17142
[17142] : 연구소 3
"""

from itertools import combinations
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
viruses = []
BLANK = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            viruses.append([i, j])
        elif arr[i][j] == 0:
            BLANK += 1


def bfs():
    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and arr[ny][nx] != 1:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
                if arr[ny][nx] != 2:
                    cnt += 1

                if cnt == BLANK:
                    answer.append(visited[ny][nx])
                    return

    answer.append(float('INF'))
    return


dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
answer = []
for comb in combinations(viruses, M):
    visited = [[0]*N for _ in range(N)]
    q = deque(comb)
    for a, b in q:
        visited[a][b] = 1
    bfs()

if BLANK == 0:
    print(0)
else:
    if min(answer) == float('INF'):
        print(-1)
    else:
        print(min(answer)-1)

