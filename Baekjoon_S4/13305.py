#30분 #그리디알고리즘
"""
https://www.acmicpc.net/problem/13305
[13305] : 주유소
"""

import sys
input = sys.stdin.readline

N = int(input())
d = list(map(int, input().split()))
c = list(map(int, input().split()))

cost = 0
minCost = c[0]

for i in range(N-1):
    if minCost > c[i]:
        minCost = c[i]
    cost += (minCost * d[i])

print(cost)