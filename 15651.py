#3분 #백트래킹
"""
https://www.acmicpc.net/problem/15651
[15651] : N과 M(3)
N과 M(1)과 상당히 유사하다
(N*M)
"""

N, M = map(int, input().split())


lst = []
def sol():
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    
    else:
        for i in range(1, N+1):
            lst.append(i)
            sol()
            lst.pop()

sol()