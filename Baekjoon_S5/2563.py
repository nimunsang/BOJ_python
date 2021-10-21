"""
https://www.acmicpc.net/problem/2563
[2563] : 색종이
"""
N = int(input())

lst = []
for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            lst.append((j, k))

s_lst = set(lst)
print(len(s_lst))