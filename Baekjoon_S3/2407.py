#1분 #수학 #다이나믹프로그래밍 #조합론 #임의정밀도/큰수연산
"""
https://www.acmicpc.net/problem/2407
[2407] : 조합
"""

from math import comb

n, m = map(int, input().split())

print(comb(n, m))