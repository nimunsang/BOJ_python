#5분 #자료구조 #해시를사용한집합과맵
"""
https://www.acmicpc.net/problem/17219
[17219] : 비밀번호 찾기
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
for i in range(N):
    link, password = input().rstrip().split()
    dic[link] = password

for i in range(M):
    l = input().rstrip()
    print(dic[l])