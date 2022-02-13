#2시간 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/17144
[17144] : 미세먼지 안녕
2차원 rotate에 대한 개념을 잡아야할듯
"""

from collections import deque
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
cleaner = []

for i in range(R):
    if arr[i][0] == -1:
        cleaner.append((i, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread():
    tmp_arr = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if arr[y][x] > 0:
                tmp = arr[y][x] // 5
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < C and 0 <= ny < R and arr[ny][nx] != -1:
                        tmp_arr[y][x] -= tmp
                        tmp_arr[ny][nx] += tmp

    for y in range(R):
        for x in range(C):
            arr[y][x] += tmp_arr[y][x]


def cleanup(y, x):
    rotation = []
    for i in range(y):
        rotation.append(arr[i][0])
    rotation.append(0)  # arr[y][0]

    for i in range(1, C):
        rotation.append(arr[y][i])
    for i in range(y-1, -1, -1):
        rotation.append(arr[i][C-1])
    for i in range(C-2, 0, -1):
        rotation.append(arr[0][i])

    rotation = deque(rotation)
    rotation.rotate(1)

    for i in range(y):
        arr[i][0] = rotation.popleft()
    rotation.popleft()
    arr[y][0] = -1

    for i in range(1, C):
        arr[y][i] = rotation.popleft()
    for i in range(y-1, -1, -1):
        arr[i][C-1] = rotation.popleft()
    for i in range(C-2, 0, -1):
        arr[0][i] = rotation.popleft()


def cleandown(y, x):
    rotation = [0]
    for i in range(1, C):
        rotation.append(arr[y][i])
    for i in range(y+1, R):
        rotation.append(arr[i][C-1])
    for i in range(C-2, -1, -1):
        rotation.append(arr[R-1][i])
    for i in range(R-2, y, -1):
        rotation.append(arr[i][0])

    rotation = deque(rotation)
    rotation.rotate(1)

    rotation.popleft()
    for i in range(1, C):
        arr[y][i] = rotation.popleft()
    for i in range(y+1, R):
        arr[i][C-1] = rotation.popleft()
    for i in range(C-2, -1, -1):
        arr[R-1][i] = rotation.popleft()
    for i in range(R-2, y, -1):
        arr[i][0] = rotation.popleft()


for _ in range(T):
    spread()
    cleanup(cleaner[0][0], cleaner[0][1])
    cleandown(cleaner[1][0], cleaner[1][1])

print(sum(map(sum, arr)) + 2)
