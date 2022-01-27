#2시간 #구현 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/2573
[2573] : 빙산
DFS --> 메모리초과가 났다.
BFS로 해결해야하는문제
"""

import sys
input = sys.stdin.readline
from collections import deque

def applycnt():
    for i in range(len(ice)):
        y, x, cnt = ice[i]
        arr[y][x] = max(arr[y][x]-cnt, 0)

def next_ice():
    new_ice = []
    for ic in ice:
        y, x = ic[0], ic[1]
        if arr[y][x] != 0:
            new_ice.append([y, x, 0])
    return new_ice

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if visited[ny][nx] == 0 and arr[ny][nx] != 0:
                q.append((ny, nx))
                visited[ny][nx] = 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ice = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            ice.append([i, j, 0])
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
day = 0

while len(ice) != 0:
    cnt = 0
    for ic in ice:
        y, x = ic[0], ic[1]
        if not visited[y][x]:
            cnt += 1
            if cnt == 2:
                print(day)
                exit(0)
            bfs(y, x)

    for i in range(len(ice)):
        y, x = ice[i][0], ice[i][1]
        visited[y][x] = 0
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 0:
                ice[i][2] += 1

    applycnt()
    ice = next_ice()
    day += 1

print(0)