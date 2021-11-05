#15분 #구간합
"""
https://www.acmicpc.net/problem/11659
[11659] : 구간 합 구하기 4
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = dp[i] + lst[i]

for i in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])