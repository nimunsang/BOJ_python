#해결 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/1697
[1697] : 숨바꼭질
"""

from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs():
    deq = deque()
    deq.append(N)
    while deq:
        d = deq.popleft()
        if d == K:
            print(visited[K])
            break

        for dn in (d-1, d+1, d*2):
            if 0<=dn<=100000 and visited[dn] == 0:
                visited[dn] = visited[d] + 1
                deq.append(dn)

bfs()