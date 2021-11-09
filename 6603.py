#20분 #수학 #조합론 #백트래킹 #재귀
"""
https://www.acmicpc.net/problem/6603
[6603] : 로또
"""
from itertools import combinations

while True:
    s = input()
    if s == '0':
        break
    else:
        s = s.split()[1:]
        c = combinations(s, 6)
        for i in c:
            print(' '.join(i))
        print()