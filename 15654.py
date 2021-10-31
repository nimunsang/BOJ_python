#5분 #백트래킹
"""
https://www.acmicpc.net/problem/15654
[15654] : N과 M(5)
N과 M시리즈에서 지금까지는 리스트가 [1부터N]으로
결정됐다면, 이번에는 주어진 리스트라는 것 말고는
다른 점이 없다.
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
            if i not in arr:
                arr.append(i)
                sol()
                arr.pop()

sol()
