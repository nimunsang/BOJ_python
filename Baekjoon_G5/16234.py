#30분 #구현 #그래프이론 #그래프탐색 #BFS #시뮬레이션
"""
https://www.acmicpc.net/problem/16234
[16234] : 인구 이동
"""

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
    global mask
    q = deque([])
    q.append([a, b])
    visited[a][b] = 1
    while q:
        a, b = q.popleft()
        area.append([a, b])
        for i in range(4):
            x = b + dx[i]
            y = a + dy[i]
            if 0<=x<N and 0<=y<N and\
                 L<=abs(arr[y][x]-arr[a][b])<=R and visited[y][x] == 0:
                 q.append([y, x])
                 visited[y][x] = 1
                 mask = 1
    
day = 0
while True:
    mask = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                area = []
                bfs(i, j)
                s = sum(arr[y][x] for y, x in area)
                
                for y, x in area:
                    arr[y][x] = s // len(area)
    
    if mask == 1:
        day += 1
    
    else:
        print(day)
        break