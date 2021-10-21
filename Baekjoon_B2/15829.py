"""
https://www.acmicpc.net/problem/15829
[15829: Hashing]
"""

N = int(input())
s = input()

L = 0
for i in range(N):
    L += (ord(s[i])-96) * (31**i)

print(L%1234567891)