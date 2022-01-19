#10분 #그래프이론 #최소스패닝트리
"""
https://www.acmicpc.net/problem/1647
[1647] : 도시 분할 계획
"""

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

heap = [[0, 1]]
cnt = 0
answer = 0
maximum = 0
while heap:
    if cnt == N:
        break

    weight, vertex = heapq.heappop(heap)
    
    if not visited[vertex]:
        visited[vertex] = 1
        cnt += 1
        answer += weight
        maximum = max(maximum, weight)
        for i in graph[vertex]:
            heapq.heappush(heap, i)

print(answer-maximum)
