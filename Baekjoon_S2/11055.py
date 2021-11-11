#20분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11055
[11055] : 가장 큰 증가 부분 수열 
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [i for i in A]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))