#다시 #그래프이론 #최소스패닝트리
"""
https://www.acmicpc.net/problem/1922
[1922] : 네트워크 연결
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

answer = 0
cnt = 0
heap = [[0, 1]]
while heap:
    if cnt == N:
        break

    cost, x = heapq.heappop(heap)
    if visited[x] == 0:
        visited[x] = 1
        answer += cost
        cnt += 1        
        for next_cost, next_x in graph[x]:
            heapq.heappush(heap, (next_cost, next_x))

print(answer)