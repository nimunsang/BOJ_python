#30분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11054
[11054] : 가장 긴 바이토닉 부분수열
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ascending = [1] * N
descending = [1]*N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            ascending[i] = max(ascending[i], ascending[j]+1)

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if arr[i] > arr[j]:
            descending[i] = max(descending[i], descending[j]+1)

print(max(map(sum, list(zip(ascending, descending))))-1)