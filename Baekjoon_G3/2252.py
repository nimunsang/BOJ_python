#해결 #그래프이론 #위상정렬
"""
https://www.acmicpc.net/problem/2252
[2252] : 줄 세우기
"""

from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

def topologysort():
    res = []
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        v = q.popleft()
        res.append(v)
        for i in graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    print(*res)

topologysort()