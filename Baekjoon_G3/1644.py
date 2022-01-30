#다시 #수학 #정수론 #두포인터 #소수판정 #에라토스테네스의 체
"""
https://www.acmicpc.net/problem/1644
[1644] : 소수의 연속합
"""

import math

N = int(input())

sosu = [1]*(N+1)
sosulist = []
for i in range(2, int(math.sqrt(N+1))+1):
        for j in range(2*i, (N+1), i):
            sosu[j] = 0

sosulist = [0] + [i for i in range(2, N+1) if sosu[i]]
L = len(sosulist)
for i in range(1, L):
    sosulist[i] += sosulist[i-1]

start = 0
end = 1
answer = 0
while end < L:
    if sosulist[end] - sosulist[start] == N:
        answer += 1
        start += 1
    else:
        if sosulist[end] - sosulist[start] > N:
            start += 1
        else:
            end += 1
print(answer)