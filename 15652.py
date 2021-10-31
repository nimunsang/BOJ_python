#3분 #백트래킹
"""
https://www.acmicpc.net/problem/15652
[15652] : N과 M(4)
N과 M(2) 와 상당히 유사하다
(중복조합개념) 
"""

N, M = map(int, input().split())

lst = []

def sol():
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    
    else:
        for i in range(1, N+1):
            if len(lst) == 0 or i >= lst[-1]:
                lst.append(i)
                sol()
                lst.pop()

sol()