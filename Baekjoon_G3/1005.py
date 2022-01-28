#1시간 #다이나믹프로그래밍 #그래프이론 #위상정렬
"""
https://www.acmicpc.net/problem/1005
[1005] : ACM Craft
"""

from collections import deque
import sys
input = sys.stdin.readline

def topology():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        v = q.popleft()
        dp[v] = max(D[v], dp[v])
        for adj in graph[v]:
            indegree[adj] -= 1
            dp[adj] = max(dp[adj], dp[v]+D[adj])
            if indegree[adj] == 0:
                q.append(adj)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    dp = [0] * (N+1)
    for i in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    W = int(input())
    topology()
    print(dp[W])