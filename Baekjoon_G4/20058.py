#1시간 #구현 #그래프이론 #그래프탐색 #BFS #시뮬레이션 #DFS
"""
https://www.acmicpc.net/problem/20058
[20058] : 마법사 상어와 파이어스톰
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
Qlist = list(map(int, input().split()))


def divide_rotate(a, l):
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            subarr = []
            for a in range(i, i+2**l):
                subline = []
                for b in range(j, j+2**l):
                    subline.append(arr[a][b])
                subarr.append(subline)

            rotate_subarr = list(zip(*subarr[::-1]))

            for a in range(i, i+2**l):
                for b in range(j, j+2**l):
                    arr[a][b] = rotate_subarr[a-i][b-j]


def reduce_ice(a):
    next_arr = []
    for i in range(2**N):
        next_line = []
        for j in range(2**N):
            cnt = 0
            for k in range(4):
                ny, nx = i+dy[k], j+dx[k]
                if 0 <= ny < 2**N and 0 <= nx < 2**N and arr[ny][nx]:
                    cnt += 1
            if cnt <= 2 and arr[i][j]:
                next_line.append(arr[i][j]-1)
            else:
                next_line.append(arr[i][j])

        next_arr.append(next_line)

    return next_arr


def find_largest(a):
    def dfs(y, x):
        nonlocal cnt
        arr[y][x] = 0

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N and arr[ny][nx]:
                dfs(ny, nx)
                cnt += 1

        return cnt

    large = 0
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j]:
                cnt = 1
                dfs(i, j)
                large = max(large, cnt)

    return large


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for l in Qlist:
    divide_rotate(arr, l)
    arr = reduce_ice(arr)


total = sum(map(sum, arr))
largest = find_largest(arr)
print(total)
print(largest)