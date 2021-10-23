"""
https://www.acmicpc.net/problem/1676
[1676] : 팩토리얼 0의 개수
"""

from math import *

N = int(input())
N = factorial(N)
N = str(N)
cnt = 0
k= 1
while True:
    if N[-k] == '0':
        cnt += 1
        k += 1
    else:
        break
print(cnt)

# ==============인터넷 풀이==========
# 이렇게 풀자
# N = int(input())
# print(N//5 + N//25 + N//125)