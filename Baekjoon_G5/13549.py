#30분 #그래프이론 #자료구조 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/13549
[13549] : 숨바꼭질 3
"""

from collections import deque

N, K = map(int, input().split())
dp = [float('inf')]*100001

def bfs(start):
    q = deque()
    q.append(start)
    dp[start] = 0
    while q:
        start = q.popleft()
        for s in [start-1, start+1, start*2]:
            if 0<=s<100001:
                if s == start*2:
                    if dp[start] < dp[s]:
                        dp[s] = dp[start]
                        q.append(s)
                
                else:
                    if dp[start]+1 < dp[s]:
                        dp[s] = dp[start]+1
                        q.append(s)

bfs(N)
print(dp[K])