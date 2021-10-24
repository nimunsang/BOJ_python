#2시간 #자료구조 #정렬 #이분탐색 #해시를사용한집합과맵
"""
https://www.acmicpc.net/problem/10816
[10816] : 숫자 카드 2
앞서 배운 counter함수를 이용하니까 너무쉽다
"""

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nlst = list(map(int, input().split()))
M = int(input())
mlst = list(map(int, input().split()))

c = Counter(nlst)

for i in mlst:
    print(c[i], end = " ")


"""
hashmap을 이용한 풀이
"""
# import sys
# input = sys.stdin.readline

# N = int(input())
# nlst = list(map(int, input().split()))
# M = int(input())
# mlst = list(map(int, input().split()))

# hashmap = {}

# for i in range(N):
#     if nlst[i] in hashmap:
#         hashmap[nlst[i]] += 1
#     else:
#         hashmap[nlst[i]] = 1

# for i in mlst:
#     if i in hashmap:
#         print(hashmap[i], end= " ")
#     else:
#         print("0", end = " ")