#해결 #수학 #정수론 #소수판정 #에라토스테네스의체
"""
https://www.acmicpc.net/problem/9020
[9020] : 골드바흐의 추측
"""

T = int(input())
isprime = [0, 0] + [1] * (10001-2)
lst = []

for i in range(2, 101):
    for j in range(i+i, 10001, i):
        if isprime[j] == 1:
            isprime[j] = 0
     
for i in range(T):
    N = int(input())

    A = N//2
    B = A

    for i in range(10001):
        if isprime[A] and isprime[B]:
            print(A, B)
            break
        
        else:
            A -= 1
            B += 1