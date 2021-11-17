#30분 #그래프이론 #그래프탐색 #너비우선탐색 #깊이우선탐색
"""
https://www.acmicpc.net/problem/2667
[2667] : 단지번호붙이기
"""

from collections import deque

N = int(input())
lst = [list(map(int, input())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, cnt):
    deq = deque([(x, y)])
    lst[x][y] = 0
    while True:
        if not deq:
            cnt_lst.append(cnt)
            break
        x, y = deq.popleft()
        cnt += 1
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a<N and 0<=b<N and lst[a][b] == 1:
                lst[a][b] = 0
                deq.append((a, b))

# def dfs(x, y, cnt):
#     global c
#     lst[x][y] = 0
#     c += 1
#     for i in range(4):
#         a = x + dx[i]
#         b = y + dy[i]
#         if 0<=a<N and 0<=b<N and lst[a][b] == 1:
#             lst[a][b] = 0
#             dfs(a, b, cnt)
    
cnt_lst = []
cnt = 0
# c = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            bfs(i, j, 0)
            cnt += 1
            # dfs(i, j, c)
            # cnt_lst.append(c)
            # c = 0

print(cnt)

for i in sorted(cnt_lst):
    print(i)