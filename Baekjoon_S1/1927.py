#자료구조 #우선순위 큐
"""
https://www.acmicpc.net/problem/1927
[1927] : 최소 힙
"""

from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())

    if x > 0:
        heappush(heap, x)
    
    elif x == 0:
        if len(heap) == 0:
            print(0)
        
        else:
            print(heappop(heap))