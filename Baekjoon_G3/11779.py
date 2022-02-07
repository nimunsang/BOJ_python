#다시 #그래프이론 #다익스트라
"""
https://www.acmicpc.net/problem/11779
[11779] : 최소비용구하기2
"""

import heapq
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))
start, end = map(int, input().split())

way = [[] for _ in range(n+1)]
way[start].append(start)

def dijkstra(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    heap = []
    heap.append((distance[start], start))
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue

        for next_dist, adj in graph[node]:
            next_weight = dist + next_dist
            if next_weight < distance[adj]:
                distance[adj] = next_weight
                heapq.heappush(heap, (next_weight, adj))
                
                way[adj] = []
                for w in way[node]:
                    way[adj].append(w)
                way[adj].append(adj)
    
    return distance

distance = dijkstra(start)
print(distance)
for w in way:
    print(w)