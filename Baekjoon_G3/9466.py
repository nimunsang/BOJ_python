#다시 #그래프이론 #그래프탐색 #DFS
"""
https://www.acmicpc.net/problem/9466
[9466] : 텀 프로젝트
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(start):
    global result
    visited[start] = 1
    lst.append(start)
    next = arr[start]

    if visited[next]:
        if next in lst:
            result += lst[lst.index(next):]
        return
    else:
        dfs(next)


for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    result = []
    for i in range(1, n+1):
        if not visited[i]:
            lst = []
            dfs(i)
    print(n - len(result))