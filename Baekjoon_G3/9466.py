#해결 #그래프이론 #그래프탐색 #DFS
"""
https://www.acmicpc.net/problem/9466
[9466] : 텀 프로젝트
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def solve(start):
    global answer
    lst.append(start)
    visited[start] = 1
    next = arr[start]

    if visited[next]:
        if next in lst:
            startind = lst.index(next)
            answer += lst[startind:]
        return
    
    else:
        solve(next)
        

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    answer = []
    
    for i in range(1, N+1):
        if not visited[i]:
            lst = []
            solve(i)
    print(N - len(answer))