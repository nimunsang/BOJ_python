# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
mask = 0
for a in arr:
    if a >= 0:
        mask = 1
if mask == 0 :
    print(max(arr))
else:
    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = max(dp[i], dp[i-1]+arr[i-1])

    print(max(dp))