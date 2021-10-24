#50분 #자료구조 #문자열 #정렬 #해시를 사용한 집합과 맵
#시간초과가 3번 났다. (정렬 방식의 문제)
#정렬을 첫 알파벳으로 쪼개서 하니 시간초과가 안났다!
#인터넷 풀이를 보니, LIST를 SET으로 바꾸어 &연산자를 사용
#LIST끼리 AND연산자를 사용하려하니 안되서 포기했었는데, 
#SET으로 바꾼다는 것을 알게 되었다.
"""
https://www.acmicpc.net/problem/1764
[1764] : 듣보잡
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
mask_lst = [[] for i in range(26)]

for i in range(N):
    s = input().rstrip()
    mask_lst[(ord(s[0])-97)].append(s)
for i in range(M):
    s = input().rstrip()
    mask_lst[(ord(s[0])-97)].append(s)

for i in mask_lst:
    i.sort()

new_lst = []
for i in mask_lst:
    for j in range(len(i)-1):
        if i[j] == i[j+1]:
            new_lst.append(i[j])

print(len(new_lst))
for i in new_lst:
    print(i)