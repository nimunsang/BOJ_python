#1시간 #이분탐색 #매개변수탐색
"""
https://www.acmicpc.net/problem/2805
[2805] : 나무 자르기
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, max(lst)

while start <= end:
    mid = (start + end) // 2  
    cost = 0
    for i in lst:
        if i >= mid:
            cost += (i - mid)

    if cost >= M:
        start = mid + 1

    else:
        end = mid - 1

print(end)