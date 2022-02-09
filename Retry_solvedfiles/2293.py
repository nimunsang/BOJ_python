# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp = [0] * (K+1)


for i in range(1, N+1):
    for j in range(1, K+1):
        if j == arr[i-1]:
            dp[j] += 1
        elif j >= arr[i-1]:
            dp[j] = dp[j] + dp[j-arr[i-1]]

print(dp[-1])