#1시간 #그래프이론 #다익스트라
"""
https://www.acmicpc.net/problem/11779
[11779] : 최소비용 구하기 2
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))
START, END = map(int, input().split())
minpath = [[] for _ in range(N+1)]

def dijkstra(s):
    distance = [float('inf')] * (N+1)
    distance[s] = 0
    heap = []
    heap.append((distance[s], s, [s]))
    while heap:
        dist, node, path = heapq.heappop(heap)
        if dist > distance[node]:
            continue
            
        for next_dist, adj in graph[node]:
            next_cost = dist + next_dist
            if next_cost < distance[adj]:
                distance[adj] = next_cost
                minpath[adj] = path + [adj]
                heapq.heappush(heap, (next_cost, adj, path + [adj]))
    
    return distance

distance = dijkstra(START)
print(distance[END])
print(len(minpath[END]))
print(*minpath[END])