#5분 #백트래킹
"""
https://www.acmicpc.net/problem/15657
[15657] : N과 M(8)
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
            if len(arr) == 0 or i >= arr[-1]:
                arr.append(i)
                sol()
                arr.pop()

sol()