# https://www.acmicpc.net/problem/1261

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if y == N-1 and x == M-1:
            print(visited[y][x]-1)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    q.appendleft((ny, nx))
                    visited[ny][nx] = visited[y][x]
                else:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1

bfs()