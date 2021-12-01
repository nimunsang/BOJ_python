#30분 #수학 #자료구조 #해시를사용한집합과맵
"""
https://www.acmicpc.net/problem/9375
[9375] : 패션왕 신해빈
"""

# from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dic = {}
    n = int(input())
    for i in range(n):
        name, kind = input().rstrip().split()

        if kind not in dic:
            dic[kind] = 1
        
        else:
            dic[kind] += 1

    lst = list(dic.values())

    res = 1
    for i in lst:  
        res *= i + 1

    print(res-1) 