# https://www.acmicpc.net/problem/1167

import heapq
import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    s = arr[0]
    j = 1
    while arr[j] != -1:
        graph[s].append((arr[j+1], arr[j]))
        j += 2

def dijkstra(start):
    distance = [float('inf')] * (V+1)
    distance[start] = 0
    heap = []
    heap.append((distance[start], start))
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]:
            continue

        for next_dist, adj in graph[node]:
            next_cost = dist + next_dist
            if next_cost < distance[adj]:
                distance[adj] = next_cost
                heapq.heappush(heap, (next_cost, adj))
    
    return distance

firstdistance = dijkstra(1)
maxnode = firstdistance.index(max(firstdistance[1:]))
maxdistance = dijkstra(maxnode)
print(max(maxdistance[1:]))