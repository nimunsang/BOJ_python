#10분 #구현 #백트래킹
"""
https://www.acmicpc.net/problem/2239
[2239] : 스도쿠
"""

N = 9
arr = [list(map(int, input())) for _ in range(N)]

def check(y, x, target):
    for i in range(N):
        if arr[y][i] == target or arr[i][x] == target:
            return False

    for i in range(y//3*3, y//3*3+3):
        for j in range(x//3*3, x//3*3+3):
            if arr[i][j] == target:
                return False

    return True


def dfs(idx):
    global answer
    if idx == len(blank):
        for a in arr:
            print(''.join(map(str, a)))
        exit(0)

    x, y = blank[idx][1], blank[idx][0]

    for k in range(1, N+1):
        if check(y, x, k):
            arr[y][x] = k
            dfs(idx+1)
            arr[y][x] = 0


blank = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            blank.append([i, j])

dfs(0)