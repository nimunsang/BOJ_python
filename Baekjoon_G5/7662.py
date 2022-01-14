#다시 #자료구조 #트리를사용한집합과맵 #우선순위큐
"""
https://www.acmicpc.net/problem/7662
[7662] : 이중 우선순위 큐
"""

import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    maxheap = []
    minheap = []
    visited = [0] * 1000001
    for i in range(k):
        c, n = input().rstrip().split()
        n = int(n)
        if c == "I":
            heapq.heappush(maxheap, (-n, i))
            heapq.heappush(minheap, (n, i))
            visited[i] = 1

        elif c == 'D':
            if n == -1:
                while minheap and not visited[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    visited[minheap[0][1]] = 0
                    heapq.heappop(minheap)
            
            elif n == 1:
                while maxheap and not visited[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]] = 0
                    heapq.heappop(maxheap)
    
    # 쓰레기값이 남아있을 수 있므로, 한번 더 제거
    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)
    
    if maxheap and minheap:
        print(-maxheap[0][0], minheap[0][0])
    
    else:
        print("EMPTY")