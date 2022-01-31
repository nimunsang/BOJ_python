#1시간 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/2146
[2146] : 다리 만들기
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mapvisited = [[0] * (N) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#===============================================inp

def makeisland(y, x, count):
    q = deque()
    q.append((y, x))
    arr[y][x] = count
    mapvisited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<N and 0<=ny<N and not mapvisited[ny][nx]:
                if arr[ny][nx] == 1:
                    mapvisited[ny][nx] = 1
                    arr[ny][nx] = count
                    q.append((ny, nx))

def bfs(y, x, startisland):
    global visited
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<N and 0<=ny<N and arr[ny][nx] != startisland and not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x]+1
                else:
                    return visited[y][x]
        
    return 500

count = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not mapvisited[i][j]:
            makeisland(i, j, count)
            count += 1

answer = 500
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            visited = [[0] * (N) for _ in range(N)]
            length = bfs(i, j, arr[i][j])
            answer = min(answer, length)

print(answer)