#1시간반 #구현
"""
https://www.acmicpc.net/problem/21608
[21608] : 상어 초등학교
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
students = [[] for _ in range(N**2+1)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check(target):
    global maxadjy, maxadjx, maxadj, maxadjcount
    global maxblanky, maxblankx, maxblank
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 0:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[ny][nx] in students[target]:
                            adj[y][x] += 1
                        if arr[ny][nx] == 0:
                            blank[y][x] += 1

                if adj[y][x] > maxadj:
                    maxadj = adj[y][x]
                    maxadjcount = 1
                    maxadjy, maxadjx = y, x
                elif adj[y][x] == maxadj:
                    maxadjcount += 1

    if maxadjcount == 1:
        arr[maxadjy][maxadjx] = target

    else:
        for y in range(N):
            for x in range(N):
                if arr[y][x] == 0 and adj[y][x] == maxadj:
                    if blank[y][x] > maxblank:
                        maxblank = blank[y][x]
                        maxblanky, maxblankx = y, x

        arr[maxblanky][maxblankx] = target


for _ in range(N**2):
    lst = list(map(int, input().split()))
    student = lst[0]
    for i in range(1, 5):
        students[student].append(lst[i])

    maxadjy, maxadjx, maxadj, maxadjcount = -1, -1, -1, -1
    maxblanky, maxblankx, maxblank = -1, -1, -1

    adj = [[0]*N for _ in range(N)]
    blank = [[0]*N for _ in range(N)]

    check(student)


answer = 0
for a in range(N):
    for b in range(N):
        cnt = 0
        for k in range(4):
            na = a + dy[k]
            nb = b + dx[k]
            if 0 <= na < N and 0 <= nb < N:
                if arr[na][nb] in students[arr[a][b]]:
                    cnt += 1

        answer += ((10**cnt) // 10)

print(answer)

