#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/1912
[1912] : 연속합
"""

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = lst[0]

for i in range(1, n):
    dp[i] = max(lst[i], dp[i-1] + lst[i])
print(max(dp))