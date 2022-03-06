# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    subtotal = [[0] * K for _ in range(K)]  # 부분 합

    for i in range(K):
        for j in range(i, K):
            if i == j:
                subtotal[i][j] = arr[j]
            else:
                subtotal[i][j] = subtotal[i][j-1] + arr[j]

    dp = [[float('inf')] * K for _ in range(K)]  #  접었을 때 비용

    for i in range(K):
        for j in range(i+1):
            dp[i][j] = 0

    for length in range(1, K):
        for i in range(K-length):
            if length == 1:
                dp[i][i+length] = subtotal[i][i+length]

            else:
                for j in range(1, i+length):
                    dp[i][i+length] = min(dp[i][i+length], dp[i][j] + dp[j+1][i+length] + subtotal[i][i+length])

    print(dp[0][K-1])