#3분 #백트래킹
"""
https://www.acmicpc.net/problem/15650
[15650] : N과 M(2)
이전 문제(N과 M(1)에서 순열을 사용한것을
응용해서, 이번 문제는 조합을 이용하였다.
이 생각이 바로나서 3분만에 문제를 해결했다.
백트래킹으로도 문제를 해결해보자)
"""

N, M = map(int, input().split())

lst = []
def dfs():
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    
    else:
        for i in range(1, N+1):
            if len(lst) == 0 or i > lst[-1]:
                lst.append(i)
                dfs()
                lst.pop()
dfs()





# from itertools import *

# N, M = map(int, input().split())

# c = combinations(range(1, N+1), M)

# for i in c:
#     print(' '.join(map(str, i)))