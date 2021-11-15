#30분 #이분탐색 #매개변수탐색
"""
https://www.acmicpc.net/problem/1654
[1654] : 랜선 자르기
"""

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(K):
        cnt += (lst[i] // mid)

    if cnt >= N:
        start = mid + 1
    
    else:
        end = mid - 1

print(end)