#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/1463
[1463] : 1로 만들기
"""

N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])