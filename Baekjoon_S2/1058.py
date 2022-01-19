#20분 #그래프이론 #브루트포스알고리즘 #그래프탐색 #DFS #플로이드-와샬
"""
https://www.acmicpc.net/problem/1058
[1058] : 친구
"""

#플로이드 - 와샬 알고리즘으로 해결했다.
N = int(input())

inf = 10**9
friends = [[inf] * (N+1) for _ in range(N+1)] 
for i in range(1, N+1):
    s = input()
    for j in range(1, N+1):
        if s[j-1] == 'Y':
            friends[i][j] = 1
        if i == j:
            friends[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

cnt = []
for i in range(1, N+1):
    c = 0
    for j in range(1, N+1):
        if 0<friends[i][j] <= 2:
            c += 1
    cnt.append(c)

print(max(cnt))