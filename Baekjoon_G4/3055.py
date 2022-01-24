#다시 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/3055
[3055] : 탈출
"""

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        y, x = q.popleft()
        if distance[beaber[0]][beaber[1]] != 0:
            return distance[beaber[0]][beaber[1]]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<C and 0<=ny<R:
                if arr[y][x] == 'S':
                    if arr[ny][nx] == 'D' or arr[ny][nx] == '.':
                        arr[ny][nx] = 'S'
                        distance[ny][nx] = distance[y][x] + 1
                        q.append((ny, nx))

                elif arr[y][x] == '*':
                    if arr[ny][nx] == '.' or arr[ny][nx] == 'S':
                        arr[ny][nx] = '*'
                        q.append((ny, nx))
    return "KAKTUS"
                        
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
distance = [[0]*C for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()
beaber = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            q.append((i, j))
        elif arr[i][j] == 'D':
            beaber = [i, j]

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            q.append((i, j))

print(bfs())