#해결 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/2206
[2206] : 벽부수고 이동하기
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)]
    visited[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][w]

        for i in range(4):
            x = b + dx[i]
            y = a + dy[i]
            if 0<=x<M and 0<=y<N:
                if arr[y][x] == 1 and w == 1:
                    visited[y][x][0] = visited[a][b][w] + 1
                    q.append([y, x, 0])
                elif arr[y][x] == 0 and visited[y][x][w] == 0:
                    q.append([y, x, w])
                    visited[y][x][w] = visited[a][b][w]+1
                
    return -1

a = bfs()
print(a)
