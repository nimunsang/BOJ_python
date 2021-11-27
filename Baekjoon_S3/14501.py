#해결 #다이나믹프로그래밍 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/14501
[14501] : 퇴사
"""
import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []

dp = [0] * (N+1)
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    if T[i] > N-i:
        T[i] = 0
        P[i] = 0  

for i in range(N-1, -1, -1):
    dp[i] = max(dp[i+1], dp[i + T[i]] + P[i])

print(dp[0])