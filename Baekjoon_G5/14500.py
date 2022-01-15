#해결 #구현 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/14500
[14500] : 테트로미노
"""

import sys
input = sys.stdin.readline

def dfs(y, x, cnt, s):
    global ans, arr_max
    if cnt == 4:
        ans = max(ans, s)
        return
    
    if s + (4-cnt)*arr_max <= ans:
        return
   
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0<=a<M and 0<=b<N and visited[b][a] == 0:
            if cnt == 2:
                visited[b][a] = 1
                dfs(y, x, cnt+1, s+arr[b][a])
                visited[b][a] = 0

            visited[b][a] = 1
            dfs(b, a, cnt+1, s+arr[b][a])
            visited[b][a] = 0
  
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0]*M for _ in range(N)]
arr_max = max(map(max, arr))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0
        
print(ans)


# =================내 처음 풀이============
# 통과했지만, 지저분해서 다른 풀이를 찾아보았다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    global s, maxs, cnt

    if cnt == 4:
        if s > maxs:
            maxs = s
        return
        
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0<=a<M and 0<=b<N and visited[b][a] == 0:
            visited[b][a] = 1
            cnt += 1
            s += arr[b][a]
            dfs(b, a)
            cnt -= 1
            s -= arr[b][a]
            visited[b][a] = 0

def Tcheck(y, x):
    global N, M
    left, right, up, down = 0, 0, 0, 0
    if x>=1:
        left = arr[y][x-1]
    if x<=M-2:
        right = arr[y][x+1]
    if y>=1:
        up = arr[y-1][x]
    if y<=N-2:
        down = arr[y+1][x]
    center = arr[y][x]
    s = left+right+up+down+center
    # ㅏ, ㅓ, ㅜ, ㅗ
    shape = [s-left, s-right, s-up, s-down]
    
    # if (y, x) in [(0, 0), (N-1, 0), (0, M-1), (N-1, M-1)]:
    #     return 0
    
    if y == 0:
        return shape[2]
    elif y == N-1:
        return shape[3]
    elif x == 0:
        return shape[0]
    elif x == M-1:
        return shape[1]
    else:
        return max(shape)
    
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        s = arr[i][j]
        visited[i][j] = 1
        maxs = 0
        cnt = 1
        dfs(i, j)
        maxs = max(maxs, Tcheck(i, j))
        if maxs > ans:
            ans = maxs
        
        visited[i][j] = 0

print(ans)
"""