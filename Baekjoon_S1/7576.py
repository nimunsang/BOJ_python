#다시 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/7576
[7576] : 토마토
"""

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

tomato = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            tomato.append((i, j))

def bfs(tomato):
    que = deque(tomato)
    while que:
        q = que.popleft()
        for i in range(4):
            a = q[0] + dx[i]
            b = q[1] + dy[i]
            if 0<=a<N and 0<=b<M and lst[a][b] == 0:
                    que.append((a, b))
                    lst[a][b] = lst[q[0]][q[1]] + 1
        
bfs(tomato)
for i in lst:
    for j in i:
        if j == 0:
            print("-1")
            exit(0)

m = max(map(max, lst))
print(m-1)