#해결 #그래프이론 #다익스트라
"""
https://www.acmicpc.net/problem/1916
[1916] : 최소비용 구하기
"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = 1000000000
arr = [[] for _ in range(N+1)]
dp = [inf for _ in range(N+1)]
for i in range(M):
    s, e, c = map(int, input().split())
    arr[s].append((e, c))
start, end = map(int, input().split())

def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        cost, n = heappop(heap)
        if dp[n] < cost:
            continue
            
        for next_n, c in arr[n]:
            next_cost = cost + c
            if next_cost < dp[next_n]:
                dp[next_n] = next_cost
                heappush(heap, (dp[next_n], next_n))

dijkstra(start)
print(dp[end])