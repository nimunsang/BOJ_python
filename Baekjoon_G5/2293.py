#해결 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/2293
[2293] : 동전1
"""
n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for i in lst:
    for j in range(1, k+1):
        if  j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])

#     1 2 3 4 5 6 7 8 9 10
# 1   1 1 1 1 1 1 1 1 1  1
# 2   0 1 1 2 2 3 3 4 4  5
# 5   0 0 0 0 1 1 2 2 3  4