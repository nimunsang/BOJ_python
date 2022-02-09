# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        print(0 if (i == j or graph[i][j] == float('inf')) else graph[i][j], end = " ")
    print('')