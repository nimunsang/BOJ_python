"""
https://www.acmicpc.net/problem/1158
[1158] : 요세푸스 문제
"""

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]

mylst = []
i = 0
for j in range(N):
    i += K-1
    if i >= len(lst):
        i = i%len(lst)
    mylst.append(lst.pop(i))
    
print("<" + ', '.join(str(i) for i in mylst) + ">")