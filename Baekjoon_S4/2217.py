#그리디 알고리즘 # 정렬
"""
https://www.acmicpc.net/problem/2217
[2217] : 로프
"""

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

lst.sort(reverse= True)

for i in range(N):
    lst[i] = lst[i]*(i+1)

print(max(lst))