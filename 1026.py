#3분..
"""
https://www.acmicpc.net/problem/1026
[1026] : 보물
"""
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort(reverse = True)
A.sort()

s = 0
for i in range(N):
    s += A[i] * B[i]
print(s)