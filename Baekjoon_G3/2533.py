#다시 #다이나믹프로그래밍 #트리 #트리에서의다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/2533
[2533] : 사회망 서비스(SNS)
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit((10**9))

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    visited[start] = 1
    dp[start][0] = 1

    for next in graph[start]:
        if not visited[next]:
            dfs(next)
            dp[start][0] += min(dp[next][0], dp[next][1])
            dp[start][1] += dp[next][0]


dfs(1)
print(min(dp[1][0], dp[1][1]))


