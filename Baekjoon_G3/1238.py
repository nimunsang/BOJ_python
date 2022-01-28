#30분 #그래프이론 #다익스트라
"""
https://www.acmicpc.net/problem/1238
[1238] : 파티
"""

import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))

def dijkstra(start):
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    heap = []
    heap.append((distance[start], start))
    while heap:
        dist, start = heapq.heappop(heap)

        if distance[start] < dist:
            continue
        
        for next_dist, adj in graph[start]:
            next_weight = dist + next_dist
            if distance[adj] > next_weight:
                distance[adj] = next_weight
                heapq.heappush(heap, (next_weight, adj))
    
    return distance

distx = dijkstra(X)
ans = 0
for i in range(1, N+1):
    if i != X:
        ans = max(ans, dijkstra(i)[X] + distx[i])
print(ans)