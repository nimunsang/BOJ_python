#20분 #숳가 #브루트포스알고리즘 #조합론 #백트래킹
"""
https://www.acmicpc.net/problem/1759
[1759] : 암호 만들기
"""

from itertools import combinations

L, C = map(int, input().split())
lst = input().split()
lst.sort()
comb = combinations(lst, L)
aeiou = ['a', 'e', 'i', 'o', 'u']

cnta = 0
for com in comb:
    for a in aeiou:
        if a in com:
            cnta += 1

    if cnta >= 1 and L - cnta >= 2:
        print(''.join(com))

    cnta = 0