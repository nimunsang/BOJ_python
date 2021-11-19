#20분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/1932
[1932] : 정수 삼각형
"""

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, N):
    for j in range(i):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        else:    
            lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])
    
    lst[i][i] += lst[i-1][i-1]

print(max(lst[-1]))