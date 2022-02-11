# https://www.acmicpc.net/problem/2206

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[[0]*2 for _ in range(M)] for __ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx][cnt]:
                if cnt == 0 and arr[ny][nx] == 1:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append((ny, nx, 1))
                
                elif arr[ny][nx] == 0:
                    visited[ny][nx][cnt] = visited[y][x][cnt] + 1
                    q.append((ny, nx, cnt))
    
    return -1

print(bfs())