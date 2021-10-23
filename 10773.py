#11분 .. pop을 써야되는데 remove를 써서 헤맸다
"""
https://www.acmicpc.net/problem/10773
[10773] : 제로
"""

import sys
input = sys.stdin.readline

K = int(input())

lst = []
for i in range(K):
    a = int(input())
    if a == 0:
        lst.pop(-1)
    else:
        lst.append(a)

print(sum(lst))