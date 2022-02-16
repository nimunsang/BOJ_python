# https://www.acmicpc.net/problem/7662

import heapq
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    minheap, maxheap = [], []
    visited = []
    K = int(input())
    for __ in range(K):
        op, n = input().rstrip().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(minheap, n)
            heapq.heappush(maxheap, -n)
            visited.append(n)
        elif op == 'D':
            if n == 1:
                if -maxheap[0] in visited:
                    p = heapq.heappop(maxheap)
                    visited.remove(-p)

                else:
                    while maxheap and -maxheap[0] not in visited:
                        heapq.heappop(maxheap)
            elif n == -1:
                if minheap[0] in visited:
                    p = heapq.heappop(minheap)
                    visited.remove(p)
                else:
                    while minheap and minheap[0] not in visited:
                        heapq.heappop(minheap)

    while -maxheap[0] not in visited:
        heapq.heappop(maxheap)
    while minheap[0] not in visited:
        heapq.heappop(minheap)

    print(-maxheap[0], minheap[0])

