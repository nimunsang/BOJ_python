#다시 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/1697
[1697] : 숨바꼭질
"""

from collections import deque
N, K = map(int, input().split())

visited = [0] * 100001

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            print(visited[K])
            break

        for i in (v-1, v+1, v*2):
            if 0<=i<=100000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] + 1

        
bfs(N)