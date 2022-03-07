#1시간반 #구현 #그래프이론 #그래프탐색 #BFS #시뮬레이션 #DFS
"""
https://www.acmicpc.net/problem/21609
[21609] : 상어 중학교
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def find_group(num, y, x):
    global cnt, rainbowcnt
    visited[y][x] = 1
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        xylist.append([y, x])
        visitednums[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if arr[ny][nx] == 0 or arr[ny][nx] == num:
                    cnt += 1
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                    if arr[ny][nx] == 0:
                        rainbowcnt += 1

    return cnt, rainbowcnt


def gravity():
    for i in range(N):
        for j in range(N-1, -1 ,-1):
            if arr[j][i] == -1:
                continue

            if arr[j][i] != -2:
                num = arr[j][i]
                arr[j][i] = -2
                while j < N and arr[j][i] == -2:
                    j += 1
                arr[j-1][i] = num


def rotate():
    return list(map(list, (zip(*arr[::-1]))))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
score = 0
while True:
    visitednums = [[0] * N for _ in range(N)]
    maxgroup = [0, 0, 0, 0] # size, rainbow, y, x
    maxxylist = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visitednums[i][j]:
                visited = [[0] * N for _ in range(N)]
                xylist = []
                cnt, rainbowcnt = 1, 0
                find_group(arr[i][j], i, j)
                curr_group = [cnt, rainbowcnt, i, j]
                for idx in range(4):
                    if curr_group[idx] > maxgroup[idx]:
                        maxgroup = curr_group
                        maxxylist = xylist
                        break
                    elif curr_group[idx] == maxgroup[idx]:
                        continue
                    else:
                        break

    if maxgroup[0] < 2:
        break

    score += maxgroup[0] ** 2
    for a, b in maxxylist:
        arr[a][b] = -2
    gravity()
    for i in range(3):
        arr = rotate()
    gravity()

print(score)
