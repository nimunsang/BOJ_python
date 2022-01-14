#30분 #그래프이론 #그래프탐색 #깊이우선탐색 #백트래킹
"""
https://www.acmicpc.net/problem/1987
[1987] : 알파벳
"""

R, C = map(int, input().split())
arr = []
for i in range(R):
    alphabet = list(input())
    arr.append(alphabet)


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
visited = [[0] * C for _ in range(R)]
ans = 0

def dfs(a, b, res):
    global ans
    visited[a][b] = 1
    if len(res) > ans:
        ans = len(res)

    for i in range(4):
        x = b + dx[i]
        y = a + dy[i]
        if 0<=x<C and 0<=y<R and not visited[y][x]:
            if arr[y][x] not in res:
                dfs(y, x, res+arr[y][x])
                visited[y][x] = 0

dfs(0, 0, arr[0][0])
print(ans)