#해결 #그래프이론 #다익스트라
"""
https://www.acmicpc.net/problem/1753
[1753] : 최단경로
"""

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

heap = []
inf = 100000000
dp = [inf] * (V+1)

#==========================================

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, n = heapq.heappop(heap)
        for n_wei, next_n in graph[n]:
            next_weight = weight + n_wei
            if next_weight < dp[next_n]:
                dp[next_n] = next_weight
                heapq.heappush(heap, (next_weight, next_n))

#============================================

dijkstra(K)
for i in dp[1:]:
    print(i if i != inf else "INF")