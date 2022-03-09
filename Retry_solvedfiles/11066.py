# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * K for _ in range(K)]
    subtotal = [0, arr[0]]
    for i in range(2, K+1):
        subtotal.append(subtotal[i-1] + arr[i-1])

    for length in range(1, K):
        for i in range(K-length):
            if length == 1:
                dp[i][i+length] = arr[i] + arr[i+length]
            else:
                dp[i][i+length] = float('inf')
                for j in range(i, i+length):
                    dp[i][i+length] = min(dp[i][i+length], dp[i][j] + dp[j+1][i+length] + subtotal[i+length+1]-subtotal[i])

    print(dp[0][-1])
