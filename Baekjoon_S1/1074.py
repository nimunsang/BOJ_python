#해결 #분할정복 #재귀
"""
https://www.acmicpc.net/problem/1074
[1074] : Z
"""

N, r, c = map(int, input().split())

ans = 0

while N != 0:
    N -= 1

    if r < 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 0

    elif r < 2**N and c >= 2**N:
        ans += (2**N) * (2**N) * 1
        c -= (2**N)

    elif r >= 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 2
        r -= (2**N)

    else:
        ans += (2**N) * (2**N) * 3
        c -= (2**N)
        r -= (2**N)
    
print(ans)