#2시간 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/20056
[20056] : 마법사 상어와 파이어볼
"""

from collections import deque
import sys

N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for __ in range(N)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
fireball = deque()
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball.append([r-1, c-1, m, s, d])


for _ in range(K):
    F = len(fireball)
    for i in range(F):
        r, c, m, s, d = fireball.popleft()

        nr = (r + dy[d]*s) % N
        nc = (c + dx[d]*s) % N
        arr[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            L = len(arr[i][j])
            if L == 0:
                continue

            elif L == 1:
                m, s, d = arr[i][j].pop()
                fireball.append([i, j, m, s, d])

            else:
                nm, ns, dirmask = 0, 0, 0
                for k in range(L):
                    m, s, d = arr[i][j].pop()
                    nm += m
                    ns += s
                    if d % 2 == 0:  # 방향이 짝수이면, -= 1
                        dirmask -= 1
                    else:
                        dirmask += 1

                nm //= 5
                ns //= L

                if nm > 0:
                    if abs(dirmask) == L:
                        for dir in [0, 2, 4, 6]:
                            fireball.append([i, j, nm, ns, dir])
                    else:
                        for dir in [1, 3, 5, 7]:
                            fireball.append([i, j, nm, ns, dir])


answer = 0
for i in range(len(fireball)):
    answer += fireball[i][2]

print(answer)
