#30분 #그래프이론 #그래프탐색 #트리 #BFS #DFS
"""
https://www.acmicpc.net/problem/11725
[11725] : 트리의 부모 찾기
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

Tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

Parents = [0] * (N+1)

def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, Tree, Parents)
for i in range(2, N+1):
    print(Parents[i])


