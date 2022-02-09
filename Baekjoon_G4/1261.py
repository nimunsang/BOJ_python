#해결 #그래프이론 #다익스트라 #0-1너비 우선 탐색
"""
https://www.acmicpc.net/problem/1261
[1261] : 알고스팟
"""

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if visited[N-1][M-1] != 0:
            print(visited[N-1][M-1]-1)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and visited[ny][nx] == 0:
                if arr[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x]
                    q.appendleft([ny, nx])
                else:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[0]*(M) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()