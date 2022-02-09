# https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
L1 = len(S1)
L2 = len(S2)

dp = [[0]*(L1+1) for _ in range(L2+1)]

for i in range(1, L2+1):
    for j in range(1, L1+1):
        if S2[i-1] == S1[j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])