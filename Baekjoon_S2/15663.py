#20분 #백트래킹
"""
https://www.acmicpc.net/problem/15663
[15663] : N과 M(9)
"""

import sys
input = sys.stdin.readline
from itertools import permutations


N, M = map(int, input().split())
lst = list(map(int, input().split()))

perlst = []
lst.sort()
c = permutations(lst, M)

for i in c:
    perlst.append(i)
        
perlst = sorted(list(set(perlst)))

for i in perlst:
    print(*i)