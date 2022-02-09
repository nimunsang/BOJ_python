# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)
bag = []
for _ in range(N):
    w, v = map(int, input().split())
    bag.append((w, v))

for weight, value in bag:
    for i in range(K, weight-1, -1):
        dp[i] = max(dp[i], value + dp[i-weight])

print(max(dp))