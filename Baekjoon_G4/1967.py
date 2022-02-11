#30분 #그래프이론 #그래프탐색 #트리 #DFS
"""
https://www.acmicpc.net/problem/1967
[1967] : 트리의 지름
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def bfs(v, distance):
    q = deque()
    q.append((v, distance))
    visited[v] = 0
    while q:
        node, dist = q.popleft()
        for next_dist, adj in graph[node]:
            if visited[adj] == -1:
                visited[adj] = dist+next_dist
                q.append((adj, dist + next_dist))


visited = [-1] * (N+1)
bfs(1, 0)
maxidx = visited.index(max(visited))

visited = [-1] * (N+1)
bfs(maxidx, 0)
print(max(visited))


# solved with dijkstra
"""
import heapq

def dijkstra(start):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    heap = [(distance[start], start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue
    
        for next_dist, adj in graph[node]:
            next_cost = dist + next_dist
            if next_cost < distance[adj]:
                distance[adj] = next_cost
                heapq.heappush(heap, (next_cost, adj))
    
    return distance
    
startdistance = dijkstra(1)
maxidx = startdistance.index(max(startdistance[1:]))
maxdistance = dijkstra(maxidx)
print(max(maxdistance[1:]))
"""