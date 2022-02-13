#1시간 #다이나믹프로그래밍 #그래프이론 #그래프탐색
"""
https://www.acmicpc.net/problem/12852
[12852] : 1로 만들기 2
"""

from collections import deque
import sys
input = sys.stdin.readline

X = int(input())

visited = [0] * (X + 1)

q = deque()
q.append((X, [X]))
visited[X] = 1
cnt = 0
while True:
    v, way = q.popleft()

    if v == 1:
        cnt = visited[v]-1
        break

    if not visited[v // 3] and v % 3 == 0:
        visited[v // 3] = visited[v] + 1
        q.append((v // 3, way + [v//3]))

    if not visited[v // 2] and v % 2 == 0:
        visited[v // 2] = visited[v] + 1
        q.append((v // 2, way + [v//2]))

    if not visited[v - 1]:
        visited[v - 1] = visited[v] + 1
        q.append((v - 1, way + [v-1]))

print(cnt)
print(' '.join(map(str, way)))