#다시 #수학 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/1057
[1057] : 토너먼트
"""

N, a, b = map(int, input().split())

cnt = 0
while a != b:
    a -= a//2
    b -= b//2
    cnt += 1

print(cnt)