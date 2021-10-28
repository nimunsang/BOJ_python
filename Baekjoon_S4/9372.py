#10분 #그래프이론 #트리
#트리가 딱 생각났다. 최소는 아무리생각해도
#n-1이었다.
"""
https://www.acmicpc.net/problem/9372
[9372] : 상근이의 여행
"""

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    for i in range(M):
        a, b = map(int, input().split())
    print(N-1)