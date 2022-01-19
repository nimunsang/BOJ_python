#다시 #그래프이론 #플로이드-와샬
"""
https://www.acmicpc.net/problem/11404
[11404] : 플로이드
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 10**9
graph = [[inf] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if i == j:
                graph[i][j] = 0

for i in range(1, n+1):
    print(*graph[i][1:])