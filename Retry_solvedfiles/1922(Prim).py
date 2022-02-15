# https://www.acmicpc.net/problem/1922

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [0] * (N+1)
answer = 0
def solve(cost, v):
    global answer
    heap = []
    heap.append((cost, v))
    while heap:
        cost, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            answer += cost
            for next_cost, next_node in graph[v]:
                heapq.heappush(heap, (next_cost, next_node))

solve(0, 1)
print(answer)