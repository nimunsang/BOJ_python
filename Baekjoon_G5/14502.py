#1시간 #그래프이론 #그래프탐색 #브루트포스알고리즘 #BFS
"""
https://www.acmicpc.net/problem/14502
[14502 : 연구소]
"""

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
maxres = 0

#startpos : 격자에서 2의 위치를 담은 arr
startpos = []
#empty : 격자에서 0의 위치를 담은 arr
empty = []
#wall_cnt : 처음 벽의 개수
wall_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            startpos.append([i, j])
        elif arr[i][j] == 0:
            empty.append([i, j])
        else:
            wall_cnt += 1
#========================================

def bfs():
    #visitcnt : 격자판에서 2의 개수를 cnt
    visitcnt = 0
    q = deque()
    for pos in startpos:
        q.append(pos)
        visited[pos[0]][pos[1]] = 1
        visitcnt += 1

    while q:
        v = q.popleft()

        for i in range(4):
            a = v[1] + dx[i]
            b = v[0] + dy[i]

            if 0<=a<M and 0<=b<N and arr[b][a] == 0 and visited[b][a] == 0:
                visited[b][a] = 1
                visitcnt += 1
                q.append([b, a])

    return visitcnt

#emptycomb에 격자판에서 0인 위치에 벽을 3개 세울수 있는 경우의 수 저장
emptycomb = combinations(empty, 3)

for comb in emptycomb:
    for i in range(3):
        arr[comb[i][0]][comb[i][1]] = 1
    
    visited = [[0]*M for _ in range(N)]

    v = bfs()

    # res = 격자판 - 2의개수 - (원래벽의개수) - (새로새운벽의개수)
    res = M*N - v - wall_cnt - 3
    if res > maxres:
        maxres = res

    for i in range(3):
        arr[comb[i][0]][comb[i][1]] = 0

print(maxres)