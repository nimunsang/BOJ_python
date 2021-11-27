#다시 #그래프이론 #플로이드-와샬

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(v):
    for i in range(N):
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            dfs(i)

visited = [0] * N
for i in range(N):
    dfs(i)
    print(*visited)
    visited = [0] * N


# =========플로이드-와샬 방법============
# 시간복잡도가 O(N**3) 이다.

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]

# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if (graph[i][k] == 1 and graph[k][j] == 1):
#                 graph[i][j] = 1

# for row in graph:
#     for col in row:
#         print(col, end = " ")
    
#     print()
