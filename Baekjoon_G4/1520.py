import sys
#다시 #다이나믹프로그래밍 #그래프이론 #그래프탐색 #DFS
"""
https://www.acmicpc.net/problem/1520
[1520] : 내리막길
"""

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[-1]*N for _ in range(M)]
def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1
    
    if visited[y][x] == -1:
        visited[y][x] = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<N and 0<=ny<M and arr[ny][nx] < arr[y][x]:
                    visited[y][x] += dfs(ny, nx)
    return visited[y][x]

print(dfs(0, 0))