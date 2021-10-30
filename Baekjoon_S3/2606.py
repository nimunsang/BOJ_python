#35분 #그래프이론 #그래프탐색 #BFS #DFS
#DFS를 배우기 전, 나만의 방식으로 풀어보았다.
"""
https://www.acmicpc.net/problem/2606
[2606] : 바이러스
"""
def sol(m, arr):
    for _ in range(m):
        for i in range(m):
            if visited[arr[i][0]] == True:
                visited[arr[i][1]] = True
            if visited[arr[i][1]] == True:
                visited[arr[i][0]] = True
    
    return visited.count(True)

N = int(input())
visited = [False] * (N+1)
visited[1] = True

M = int(input())
arr = []
for i in range(M):
    l = list(map(int, input().split()))
    arr.append(l)

print(sol(M, arr) - 1)


"""
<DFS를 이용한 풀이>

dic = {}
M = int(input())
for i in range(M):
    dic[i+1] = set()

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

visited = []
dfs(1, dic)
print(len(visited) - 1)
"""