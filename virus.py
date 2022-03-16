from collections import deque
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def subsafearea(y, x, visited):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    cnt = 1
    issafe = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if arr[ny][nx] == 2:
                    issafe = 0
                elif arr[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    cnt += 1
    if issafe:
        return cnt
    else:
        return 0


def findsafearea():
    global answer
    visited = [[0] * M for _ in range(N)]
    safearea = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 0:
                safearea += subsafearea(i, j, visited)

    answer = max(answer, safearea)
    if safearea == 9:
        for a in arr:
            print(*a)


def makewalls(cnt):
    blank = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                blank.append([i, j])

    comb = combinations(blank, cnt)

    for c in comb:
        for y, x in c:
            arr[y][x] = 1

        findsafearea()

        for y, x in c:
            arr[y][x] = 0


answer = 0
makewalls(3)
print(answer)
