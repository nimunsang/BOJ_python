#해결 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/1012
[1012] : 유기농 배추
연결 노드의 개수를 묻는 문제이다.
기본적인 dfs, bfs문제이므로, 두 가지 방법 모두를
사용하여 문제를 풀어보겠다
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (M+1) for _ in range(N+1)]

    # def dfs(p, q):
    #     for i in range(4):
    #         a = q + dx[i]
    #         b = p + dy[i]
    #         if graph[b][a] == 1 and (a >= 0 and b >= 0):
    #             graph[b][a] = 0
    #             dfs(b, a)

    def bfs(p, q):
        que = [(p, q)]
        while que:
            v = que.pop(0)
            for i in range(4):
                a = v[0] + dx[i]
                b = v[1] + dy[i]
                if a>=0 and b>=0 and graph[a][b] == 1:
                    graph[a][b] = 0
                    que.append((a, b))

            
            
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)