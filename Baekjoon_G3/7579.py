#30분 #다이나믹프로그래밍 #배낭문제
"""
https://www.acmicpc.net/problem/7579
[7579] : 앱
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0]+list(map(int, input().split()))
maxcost = sum(cost)
dp = [[0] * (maxcost+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(maxcost+1):
        if j >= cost[i]:
            dp[i][j] = max(mem[i]+dp[i-1][j-cost[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(1, maxcost+1):
    if dp[-1][i] >= M:
        print(i)
        break