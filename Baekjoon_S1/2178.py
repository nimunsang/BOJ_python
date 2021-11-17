#다시 #그래프이론 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/2178
[2178] : 미로 탐색

DFS알고리즘 특성상 최단거리를 찾으려면,,
완전탐색을 해야하고, 그 중에서 최솟값을 선택해야한다.
경로가 아주 많을 수 있으므로, 시간 복잡도가 매우 커진다.
반면, BFS는 최단거리를 보장하기 때문에,
최단거리 구하기 문제는 BFS로 풀어야 한다.
"""

from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    deq = deque([(x, y)])
    visited[x][y] = 1
    while deq:
        v = deq.popleft()
        if v == [N-1, M-1]:
            break

        for i in range(4):
            a = v[0] + dx[i]
            b = v[1] + dy[i]

            if 0<=a<N and 0<=b<M and lst[a][b] == 1 \
                and visited[a][b] == 0:
                visited[a][b] = visited[v[0]][v[1]] + 1
                deq.append((a, b))

bfs(0, 0)
print(visited[N-1][M-1])