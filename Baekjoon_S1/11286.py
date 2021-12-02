#10분 #자료구조 #우선순위큐
"""
https://www.acmicpc.net/problem/11286
[11286] : 절댓값 힙
"""

import sys
input = sys.stdin.readline

import heapq

N = int(input())

heap = []
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    
    else:
        if len(heap) == 0:
            print(0)

        else:
            print(heapq.heappop(heap)[1])