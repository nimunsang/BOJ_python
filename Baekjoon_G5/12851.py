#다시 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/12851
[12851] : 숨바꼭질 2
"""

from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)
visited = [0]*100001
visited[N] = 1
dp = [0]*100001
dp[N] = 1

while q:
    v = q.popleft()

    for next_v in [v+1, v-1, v*2]:
        if 0 <= next_v <= 100000:
            if not visited[next_v]:
                visited[next_v] = visited[v] + 1
                dp[next_v] = dp[v]
                q.append(next_v)
            
            elif visited[next_v] == visited[v] + 1:
                dp[next_v] += dp[v]


print(visited[K]-1)        
print(dp[K])