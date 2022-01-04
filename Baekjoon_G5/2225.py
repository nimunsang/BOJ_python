#10분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/2225
[2225] : 합분해
"""

N, K = map(int, input().split())

dp = [[0]*K for _ in range(N)]

dp[0] = [i for i in range(1, K+1)]
for i in range(N):
    dp[i][0] = 1


for i in range(1, N):
    for j in range(1, K):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] 

print(dp[-1][-1]%1000000000)