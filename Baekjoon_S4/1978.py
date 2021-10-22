"""
https://www.acmicpc.net/problem/1978
[1978] : 소수 찾기
"""

N = int(input())
lst = list(map(int, input().split()))

def is_sosu(n):
    mask = 0
    for i in range(1, n+1):
        if n%i == 0: 
            mask += 1
    return mask == 2

cnt = 0
for i in lst:
    if is_sosu(i):
        cnt += 1

print(cnt)