#20분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/1904
[1904] : 01타일
"""

N = int(input())
dp = [1, 1]
for i in range(1, N):
        dp.append((dp[i-1]+dp[i])%15746)

print(dp[-1])