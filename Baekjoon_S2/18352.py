#10분 #그래프이론 #그래프탐색 #BFS #다익스트라
"""
https://www.acmicpc.net/problem/18352
[18352] : 특정 거리의 도시 찾기
"""

import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
inf = 10**7
graph = [[] for _ in range(N+1)]
dp = [inf] * (N+1)
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append((1, B))

def dijkstra(start):
    dp[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        weight, vertex = heapq.heappop(q)

        if weight > dp[vertex]:
            continue

        for next_weight, adjacent in graph[vertex]:
            cost = next_weight + weight
            if cost < dp[adjacent]:
                dp[adjacent] = cost
                heapq.heappush(q, (cost, adjacent))

dijkstra(X)
mask = 0
for i in range(1, N+1):
    if dp[i] == K:
        print(i)
        mask = 1
if mask == 0:
    print(-1)