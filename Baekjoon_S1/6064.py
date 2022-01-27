#해결 #수학 #정수론 #중국인의나머지정리
"""
https://www.acmicpc.net/problem/6064
[6064] : 카잉 달력
"""

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())

    while x <= N*M:
        if (x-y) % N == 0:
            print(x)
            break

        x += M
    
    else:
        print(-1)