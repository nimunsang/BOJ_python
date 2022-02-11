#해결 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/2579
[2579] : 계단 오르기
"""

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

if N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
else:
    dp = []
    dp.append(scores[0])
    dp.append(max(dp[0] + scores[1], scores[1]))
    dp.append(max(dp[0] + scores[2], scores[1]+scores[2]))

    for i in range(3, N):
        dp.append(max(dp[i-2] + scores[i],\
            dp[i-3]+scores[i]+scores[i-1]))

    print(dp[-1])