#1시간 #BFS
"""
https://www.acmicpc.net/problem/7562
[7562] : 나이트의 이동
"""

import sys
sys.setrecursionlimit(100000)

T = int(input())

for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    dp = [[0] * I for _ in range(I)]

    def bfs(start, end):
        que = [[start[0], start[1]]]
        dp[start[0]][start[1]] = 1
        dx = [2, 2, 1, 1, -1, -1, -2, -2]
        dy = [1, -1, 2, -2, 2, -2, 1, -1]
        mask = 0
        while que:
            s = que.pop(0)
            if [s[0], s[1]] == end:
                print(dp[s[0]][s[1]] - 1)
                mask = 1
                break
            for i in range(8):
                p = s[0] + dx[i]
                q = s[1] + dy[i]
                if 0<=p<I and 0<=q<I and dp[p][q] == 0:
                    dp[p][q] = dp[s[0]][s[1]] + 1
                    que.append([p, q])

            if mask == 1:
                break

    bfs(start, end)