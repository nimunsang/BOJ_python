#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/10942
[10942] : 팰린드롬?
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [0]+list(map(int, input().split()))
M = int(input())
dp = [[0]*(N+1) for _ in range(N+1)]

for length in range(1, N+1):
    for start in range(1, N-length+2):
        if length == 1:
            dp[start][start] = 1
        
        elif length == 2:
            if arr[start] == arr[start+1]:
                dp[start][start+1] = 1
        
        else:
            if dp[start+1][start+length-2] == 1:
                if arr[start] == arr[start+length-1]:
                    dp[start][start+length-1] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])