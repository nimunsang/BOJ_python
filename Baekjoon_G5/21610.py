#2시간 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/21610
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # (0~8)
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


for _ in range(M):
    next_clouds = []
    d, s = map(int, input().split())

    visited = [[0]*N for _ in range(N)]

    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + directions[d][0]*s) % N
        clouds[i][1] = (clouds[i][1] + directions[d][1]*s) % N
        arr[clouds[i][0]][clouds[i][1]] += 1
        visited[clouds[i][0]][clouds[i][1]] = 1

    for y, x in clouds:
        for dy, dx in [directions[2], directions[4], directions[6], directions[8]]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 0:
                arr[y][x] += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                next_clouds.append([i, j])

    clouds = next_clouds


print(sum(map(sum, arr)))
