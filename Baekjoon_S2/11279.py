#다시 #자료구조 #우선순위큐
"""
https://www.acmicpc.net/problem/11279
[11279] : 최대 힙
"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap)[1])
        
    else:
        heapq.heappush(heap, (-x, x))