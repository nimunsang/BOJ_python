#30분 #DFS #BFS
"""
https://www.acmicpc.net/problem/4963
[4963] : 섬의 개수
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    else:

        def dfs(a, b):
            dx = [0, 0, 1, 1, 1, -1, -1, -1]
            dy = [1, -1, 1, 0, -1, 1, 0, -1]

            for i in range(8):
                p = a + dx[i]
                q = b + dy[i]

                for j in range(1, h+1):
                    if 0 <= a < h and 0<=b<w and graph[p][q] == 1:
                        graph[p][q] = 0
                        dfs(p, q)


        graph = [[0] * (w+1) for _ in range(h+1)]
        visited = [0] * (h+1)                
        lst = []
        for i in range(h):
            l = list(map(int, input().split()))
            lst.append(l)
            for j in range(len(l)):
                if l[j] == 1:
                    graph[i][j] = 1

        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        
        print(cnt)        



       