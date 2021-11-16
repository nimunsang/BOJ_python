#다시 #순열사이클분할
"""
https://www.acmicpc.net/problem/10451
[10451] : 순열 사이클
일반적인 이차원graph로는 시간초과가 났고,
'순열' 사이클임을 인지하자
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())
for i in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    #여기부터는 연결노드 개수 구하는거랑 같다!

    visited = [0] * (N+1)

    def dfs(start):
        visited[start] = 1
        next = lst[start]
        if visited[next] == 0:
            dfs(next)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt +=1     
    print(cnt)
