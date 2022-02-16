#10분 #자료구조 #정렬 #해시를사용한집합과맵
"""
https://www.acmicpc.net/problem/11652
[11652] : 카드
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
dic = dict()

for i in range(N):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1


print(sorted(dic.items(), key=lambda x:(x[1], -x[0]), reverse = True)[0][0])
