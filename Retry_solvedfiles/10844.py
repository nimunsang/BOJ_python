# https://www.acmicpc.net/problem/10844

N = int(input())

dp = [[0]*10 for _ in range(N)]
dp[0] = [0] + [1 for _ in range(1, 10)]
for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1])%1000000000)