#1103 #수학 #정수론 #소수판정 #에라토스테네스의 체
"""
https://www.acmicpc.net/problem/1929
[1929] : 소수 구하기
"""

M, N = map(int, input().split())

lst = [False, False] + [True] * (N-1)
primes = []

for i in range(2, N+1):
    if lst[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            lst[j] = False

for prime in primes:
    if M <= prime <= N:
        print(prime)
