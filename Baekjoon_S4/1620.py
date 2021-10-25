#10분 #자료구조 #해시를 사용한 집합과 맵
"""
https://www.acmicpc.net/problem/1620
[1620] : 나는야 포켓몬 마스터 이다솜
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numdic = {}
strdic = {}
for i in range(N):
    s = input().rstrip()
    numdic[i+1] = s
    strdic[s] = i+1


for i in range(M):
    s = input().rstrip()
    if s.isnumeric() == True:
        print(numdic[int(s)])
    else:
        print(strdic[s])