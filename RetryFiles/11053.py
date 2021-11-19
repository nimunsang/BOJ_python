#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11053
[11053] : 가장 긴 증가하는 부분 수열
"""
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))