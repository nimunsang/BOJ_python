#다시 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/1012
[1012] : 유기농 배추
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

def dfs(a, b):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        p = a + dx[i]
        q = b + dy[i]

        if 0 <= p < N and 0 <= q < M and graph[p][q] == 1:
            graph[p][q] = 0
            dfs(p, q)

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)