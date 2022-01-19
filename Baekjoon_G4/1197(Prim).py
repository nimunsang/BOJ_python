#다시 #그래프이론 #최소 스패닝 트리
"""
https://www.acmicpc.net/problem/1197
[1197] : 최소 스패닝 트리
"""

import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
visited = [False] * (V+1)
Elist = [[] for _ in range(V+1)]
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])

answer = 0
cnt = 0
while heap:
    if cnt == V:
        break

    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(answer)