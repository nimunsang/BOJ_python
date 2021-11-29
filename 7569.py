#1시간 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/7569
[7569] : 토마토
"""

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

arr = []
q = deque()
for i in range(H):
    l = []
    for j in range(N):
        l.append(list(map(int, input().split())))
        for k in range(M):
            if l[j][k] == 1:
                q.append([i, j, k])
    arr.append(l)

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

def bfs():
    while q:  
        v = q.popleft()
        for i in range(6):
            x = v[2] + dx[i]
            y = v[1] + dy[i]
            z = v[0] + dz[i]

            if 0<=x<M and 0<=y<N and 0<=z<H and arr[z][y][x] == 0:
                    arr[z][y][x] = arr[v[0]][v[1]][v[2]] + 1
                    q.append([z, y, x])
                
day = 0
bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)
            day = max(day, arr[i][j][k])

print(day-1)