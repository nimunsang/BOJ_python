#1시간 #그래프이론 #그래프탐색 #브루트포스알고리즘 #BFS #DFS
"""
https://www.acmicpc.net/problem/2468
[2468] : 안전 영역
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, arr))
min_height = min(map(min, arr))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
 
def dfs(x, y, height):
    visited[x][y] = 1

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if 0<=a<N and 0<=b<N and arr[a][b] > height and visited[a][b] == 0:
            visited[a][b] = 1
            dfs(a, b, height)

res = 0
for height in range(min_height-1, max_height+1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and visited[i][j] == 0:
                dfs(i, j, height)
                cnt += 1
    if cnt > res:
        res = cnt

print(res)