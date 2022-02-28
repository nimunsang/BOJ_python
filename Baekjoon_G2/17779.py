#2시간 #구현 #브루트포스알고리즘 #구현
"""
https://www.acmicpc.net/problem/17779
[17779] : 게리맨더링 2
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def make_xyd1d2():
    xyd1d2 = []
    for x in range(N):
        for y in range(N):
            for d1 in range(1, N-1):
                for d2 in range(1, N-1):
                    xyd1d2.append([x, y, d1, d2])

    final_xyd1d2 = []
    for x, y, d1, d2 in xyd1d2:
        if x + d1 + d2 <= N-1 and 1 <= y-d1 and y+d2 <= N-1:
            final_xyd1d2.append([x, y, d1, d2])

    return final_xyd1d2


def make_border(x, y, d1, d2):
    x -= 1
    y -= 1
    for i in range(d1+1):
        visited[x+i][y-i] = 5

    for i in range(d2+1):
        visited[x+i][y+i] = 5

    for i in range(d2+1):
        visited[x+d1+i][y-d1+i] = 5

    for i in range(d1+1):
        visited[x+d2+i][y+d2-i] = 5


def divide(x, y, d1, d2):
    x -= 1
    y -= 1
    for r in range(x+d1):
        for c in range(y+1):
            if visited[r][c] != 0:
                break
            visited[r][c] = 1

    for r in range(x+d2+1):
        for c in range(N-1, -1, -1):
            if visited[r][c] != 0:
                break
            visited[r][c] = 2

    for r in range(x+d1, N):
        for c in range(y-d1+d2):
            if visited[r][c] != 0:
                break
            visited[r][c] = 3

    for r in range(x+d2+1, N):
        for c in range(N-1, -1, -1):
            if visited[r][c] != 0:
                break
            visited[r][c] = 4


answer = float('INF')
xyd1d2 = make_xyd1d2()
for x, y, d1, d2 in xyd1d2:
    visited = [[0]*N for _ in range(N)]
    make_border(x, y, d1, d2)
    divide(x, y, d1, d2)

    result = [0, 0, 0, 0, 0]

    for i in range(N):
        for j in range(N):
            result[visited[i][j]%5] += arr[i][j]

    answer = min(answer, max(result) - min(result))


print(answer)
