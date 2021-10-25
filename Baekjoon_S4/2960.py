#30분 #수학 #구현 #정수론 #소수 판정 #에라토스테네스의 체
"""
https://www.acmicpc.net/problem/2960
[2960] : 에라토스테네스의 체
"""

N, K = map(int, input().split())

t = [True] * (N+1)

cnt = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if t[j]:
            t[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break