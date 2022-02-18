#1시간 #구현 #브루트포스알고리즘 #시뮬레이션
"""
https://www.acmicpc.net/problem/15683
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cctvs = []


def checkdirection(y, x, dir):
    if dir == 'left':
        for i in range(x-1, -1, -1):
            if arr[y][i] == 6:
                break
            visited[y][i] += 1

    elif dir == 'right':
        for i in range(x+1, M):
            if arr[y][i] == 6:
                break
            visited[y][i] += 1

    elif dir == 'up':
        for i in range(y-1, -1, -1):
            if arr[i][x] == 6:
                break
            visited[i][x] += 1

    elif dir == 'down':
        for i in range(y+1, N):
            if arr[i][x] == 6:
                break
            visited[i][x] += 1


def cleardirection(y, x, dir):
    if dir == 'left':
        for i in range(x-1, -1, -1):
            if arr[y][i] == 6:
                break
            visited[y][i] -= 1

    elif dir == 'right':
        for i in range(x+1, M):
            if arr[y][i] == 6:
                break
            visited[y][i] -= 1

    elif dir == 'up':
        for i in range(y-1, -1, -1):
            if arr[i][x] == 6:
                break
            visited[i][x] -= 1

    elif dir == 'down':
        for i in range(y+1, N):
            if arr[i][x] == 6:
                break
            visited[i][x] -= 1


def dfs(idx):
    global answer
    if idx == len(cctvs):
        answer = min(answer, sum(map(lambda x: x.count(0), visited)))
        return

    y, x, num = cctvs[idx]
    if num == 1:
        checkdirection(y, x, 'left')
        dfs(idx+1)
        cleardirection(y, x, 'left')

        checkdirection(y, x, 'right')
        dfs(idx+1)
        cleardirection(y, x, 'right')

        checkdirection(y, x, 'down')
        dfs(idx+1)
        cleardirection(y, x, 'down')

        checkdirection(y, x, 'up')
        dfs(idx+1)
        cleardirection(y, x, 'up')

    elif num == 2:
        checkdirection(y, x, 'up')
        checkdirection(y, x, 'down')
        dfs(idx+1)
        cleardirection(y, x, 'up')
        cleardirection(y, x, 'down')

        checkdirection(y, x, 'left')
        checkdirection(y, x, 'right')
        dfs(idx+1)
        cleardirection(y, x, 'left')
        cleardirection(y, x, 'right')

    elif num == 3:
        checkdirection(y, x, 'up')
        checkdirection(y, x, 'right')
        dfs(idx + 1)
        cleardirection(y, x, 'up')
        cleardirection(y, x, 'right')

        checkdirection(y, x, 'right')
        checkdirection(y, x, 'down')
        dfs(idx + 1)
        cleardirection(y, x, 'right')
        cleardirection(y, x, 'down')

        checkdirection(y, x, 'down')
        checkdirection(y, x, 'left')
        dfs(idx + 1)
        cleardirection(y, x, 'down')
        cleardirection(y, x, 'left')

        checkdirection(y, x, 'left')
        checkdirection(y, x, 'up')
        dfs(idx + 1)
        cleardirection(y, x, 'left')
        cleardirection(y, x, 'up')

    elif num == 4:
        checkdirection(y, x, 'up')
        checkdirection(y, x, 'right')
        checkdirection(y, x, 'left')
        dfs(idx + 1)
        cleardirection(y, x, 'up')
        cleardirection(y, x, 'right')
        cleardirection(y, x, 'left')

        checkdirection(y, x, 'right')
        checkdirection(y, x, 'up')
        checkdirection(y, x, 'down')
        dfs(idx + 1)
        cleardirection(y, x, 'right')
        cleardirection(y, x, 'up')
        cleardirection(y, x, 'down')

        checkdirection(y, x, 'down')
        checkdirection(y, x, 'left')
        checkdirection(y, x, 'right')
        dfs(idx + 1)
        cleardirection(y, x, 'down')
        cleardirection(y, x, 'left')
        cleardirection(y, x, 'right')

        checkdirection(y, x, 'left')
        checkdirection(y, x, 'up')
        checkdirection(y, x, 'down')
        dfs(idx + 1)
        cleardirection(y, x, 'left')
        cleardirection(y, x, 'up')
        cleardirection(y, x, 'down')

    elif num == 5:
        checkdirection(y, x, 'left')
        checkdirection(y, x, 'up')
        checkdirection(y, x, 'down')
        checkdirection(y, x, 'right')
        dfs(idx+1)
        cleardirection(y, x, 'left')
        cleardirection(y, x, 'up')
        cleardirection(y, x, 'down')
        cleardirection(y, x, 'right')


answer = N*M
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] in range(1, 6):
            cctvs.append((i, j, arr[i][j]))
            visited[i][j] = 1
        elif arr[i][j] == 6:
            visited[i][j] = 1


dfs(0)
print(answer)
