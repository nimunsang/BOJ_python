# 1시간..
# 1트 : 시간초과 (리스트 이용)
# 2트 : 맞왜틀 -> 찾아보니 deque의 개념을 알게됨
"""
https://www.acmicpc.net/problem/2164
[2164] : 카드2
"""

from collections import *

N = int(input())

lst = [i for i in range(1, N+1)]
lst = deque(lst)

while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())

print(lst[0])