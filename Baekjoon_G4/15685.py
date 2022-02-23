#다시 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/15685
[15685] : 드래곤 커브
"""

import sys
input = sys.stdin.readline

N = int(input())
directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
visited = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    move = [d]
    visited[y][x] = 1

    for i in range(g):
        for j in range(len(move)-1, -1, -1):
            move.append((move[j]+1)%4)

    for i in range(len(move)):
        x += directions[move[i]][1]
        y += directions[move[i]][0]
        if 0 <= x <= 100 and 0 <= y <= 100:
            visited[y][x] = 1

answer = 0
for i in range(1, 101):
    for j in range(1, 101):
        if visited[i-1][j-1] == 1 and visited[i][j-1] == 1 and \
            visited[i-1][j] == 1 and visited[i][j] == 1:
            answer += 1

print(answer)
