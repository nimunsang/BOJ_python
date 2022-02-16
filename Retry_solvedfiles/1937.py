# https://www.acmicpc.net/problem/1937

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(y, x):
    if visited[y][x]: return visited[y][x]
    visited[y][x] = 1
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] > arr[y][x]:
            visited[y][x] = max(visited[y][x], dfs(ny, nx)+1)
            dfs(ny, nx)

    return visited[y][x]


answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)














"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] > arr[y][x]:
                    if visited[ny][nx] < visited[y][x] + 1:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny, nx))


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

print(max(map(max, visited)))
"""
