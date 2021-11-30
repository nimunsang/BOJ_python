#30분 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/2583
[2583] : 영역 구하기
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(K)]
filled = [[0] * N for _ in range(M)]

for s in squares:
    for i in range(s[1], s[3]):
        for j in range(s[0], s[2]):
            filled[i][j] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global res
    filled[x][y] = 1
    res += 1
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0<=a<M and 0<=b<N and filled[a][b] == 0:
            dfs(a, b)

result = []
for i in range(M):
    for j in range(N):
        if filled[i][j] == 0:
            res = 0
            dfs(i, j)
            result.append(res)

print(len(result))
print(*sorted(result))