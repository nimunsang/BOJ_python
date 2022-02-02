#다시 #다이나믹프로그래밍 #그래프이론 #위상정렬
"""
https://www.acmicpc.net/problem/1516
[1516] : 개임 개발
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
cost = [0] * (N+1)
dp = [0] * (N+1)
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    cost[i] += lst[0]
    inp = lst[1:-1]
    for ip in inp:
        graph[ip].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        dp[i] = cost[i]
        q.append(i)

result = []
while q:
    start = q.popleft()
    result.append(start)
    for adj in graph[start]:
        indegree[adj] -= 1
        dp[adj] = max(dp[start] + cost[adj], dp[adj])
        if indegree[adj] == 0:
            q.append(adj)

for i in range(1, N+1):
    print(dp[i])