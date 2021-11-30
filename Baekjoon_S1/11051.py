#1분 #수학 #다이나믹프로그래밍 #조합론
"""
https://www.acmicpc.net/problem/11051
[11051 : 이항계수]
"""

from math import comb
N, K = map(int, input().split())
c = comb(N, K)
print(c%10007)