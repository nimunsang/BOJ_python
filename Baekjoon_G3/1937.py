#해결 #다이나믹프로그래밍 #그래프이론 #그래프탐색 #DFS
"""
https://www.acmicpc.net/problem/1937
[1937] : 욕심쟁이 판다
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    if dp[y][x] == 0:
        dp[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and arr[ny][nx] > arr[y][x]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx))

    return dp[y][x]+1

dp = [[0]*N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))
print(answer-1)