#1시간 #그래프이론 #다익스트라
"""
https://www.acmicpc.net/problem/1504
[1504] : 특정한 최단 경로
"""

import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (N+1) 
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        weight, start = heapq.heappop(heap)
        for wei, adj in graph[start]:
            next_weight = weight + wei
            if distance[adj] > next_weight:
                distance[adj] = next_weight
                heapq.heappush(heap, (next_weight, adj))
    return distance

start = dijkstra(1)
d1 = dijkstra(v1)
d2 = dijkstra(v2)

ans = min(start[v1]+d1[v2]+d2[N], start[v2]+d2[v1]+d1[N])
print(ans if ans != float('inf') else -1)