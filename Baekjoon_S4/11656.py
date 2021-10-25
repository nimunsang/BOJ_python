#4분 #문자열 #정렬
"""
https://www.acmicpc.net/problem/11656
[11656] : 접미사 배열
"""
S = input()

lst = []
for i in range(len(S)):
    lst.append(S[i:])

lst.sort()

for i in lst:
    print(i)