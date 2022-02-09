#해결 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11057
[11057] : 오르막 수
"""
N = int(input())

dp = [0] * 1001
dp[1] = 10

for i in range(2, N+1):
    dp[i] = dp[i-1]*(10+i-1) // (i)

print(dp[N]%10007)


# ===========인터넷 풀이==============
# N = int(input())

# dp = list([[1] * 10])

# for _ in range(N):
#     dp.append(list([0] * 10))

# for i in range(1, N+1):
#     for j in range(0, 10):
#         for col in range(j+1):
#             dp[i][j] += dp[i-1][col]

# print(dp[n][9] % 10007)