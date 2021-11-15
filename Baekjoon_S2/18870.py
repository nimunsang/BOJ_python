#20분 #정렬 #값/좌표 압축
"""
https://www.acmicpc.net/problem/18870
[18870] : 좌표 압축
"""

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

sortedlst = sorted(lst)
mylst = []

dict = {}

idx = 0
dict[sortedlst[0]] = 0

cnt = 1
for i in range(1, N):
    if sortedlst[i] != sortedlst[i-1]:
        dict[sortedlst[i]] = cnt
        cnt += 1
    

for i in range(N):
    print(dict[lst[i]], end = " ")