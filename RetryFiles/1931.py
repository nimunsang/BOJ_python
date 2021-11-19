#다시 #그리디알고리즘 #정렬
"""
https://www.acmicpc.net/problem/1931
[1931] : 회의실 배정
"""

import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x:(x[1], x[0]))

last = 0
cnt = 0

for i, j in lst:
    if i >= last:
        cnt += 1
        last = j

print(cnt) 