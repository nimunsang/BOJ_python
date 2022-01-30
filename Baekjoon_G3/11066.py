#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11066
[11066] : 파일 합치기
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    for i in range(1, K+1):
        arr[i] += arr[i-1]
    
    dp = [[0]*(K+1) for _ in range(K+1)]

    for i in range(2, K+1):
        for j in range(1, K-i+2):
            dp[j][i+j-1] = min(dp[j][j+k]+dp[j+k+1][i+j-1] for k in range(i-1)) + arr[j+i-1]-arr[j-1]

    print(dp[1][-1])
