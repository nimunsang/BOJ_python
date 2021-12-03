#다시
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ladder = []
for _ in range(N+M):
    a, b = map(int, input().split())
    ladder.append((a, b))

visited = [0] * 101

q = deque()
q.append(1)
visited[1] = 1
while q:
    v = q.popleft()

    for i in range(1, 7):
        if v+i <= 100 and visited[v+i] == 0:
            visited[v+i] = visited[v] + 1
            for x, y in ladder:
                if v+i == x:
                    q.append(y)
                    visited[y] = visited[x]

            else:
                q.append(v+i)

print(visited[100]-1)