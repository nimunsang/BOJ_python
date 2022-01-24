#다시 #두포인터
"""
https://www.acmicpc.net/problem/1806
[1806] : 부분합
"""

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
res = 0

minimum = float('INF')
while True:
    if res >= S:
        minimum = min(minimum, end-start)
        res -= arr[start]
        start += 1
    
    elif end == N:
        break
    
    else:
        res += arr[end]
        end += 1

if minimum == float('INF'):
    print("0")
else:
    print(minimum)