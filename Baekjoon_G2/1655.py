#다시 #자료구조 #우선순위큐
"""
https://www.acmicpc.net/problem/1655
[1655] : 가운데를 말해요
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
leftheap, rightheap, answer = [], [], []
for i in range(N):
    num = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)

    elif len(leftheap) != len(rightheap):
        heapq.heappush(rightheap, num)

    if rightheap and rightheap[0] < -leftheap[0]:
        left = heapq.heappop(leftheap)
        right = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -right)
        heapq.heappush(rightheap, -left)

    print(-leftheap[0])