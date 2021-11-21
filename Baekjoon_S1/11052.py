#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11052
[11052] : 카드 구매하기
"""

N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * 1001

dp[1] = P[1]
for i in range(2, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + P[j]:
            dp[i] = dp[i-j] + P[j]
        
print(dp[N])