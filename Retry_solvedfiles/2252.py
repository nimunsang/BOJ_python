# https://www.acmicpc.net/problem/2252

from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

answer = []
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    answer.append(v)
    for next_v in graph[v]:
        indegree[next_v] -= 1
        if indegree[next_v] == 0:
            q.append(next_v)

print(*answer)