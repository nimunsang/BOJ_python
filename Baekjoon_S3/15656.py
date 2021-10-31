#5분 #백트래킹
"""
https://www.acmicpc.net/problem/15656
[15656] : N과 M(7)
"""

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
arr = []

def sol():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    else:
        for i in lst:
            arr.append(i)
            sol()
            arr.pop()

sol()