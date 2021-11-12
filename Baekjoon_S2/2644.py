#40분 #그래프이론 #그래프탐색 #BFS #DFS
"""
https://www.acmicpc.net/problem/2644
[2644] : 촌수계산
"""

import sys
input = sys.stdin.readline

n = int(input())
target1, target2 = map(int, input().split())
check = [0] * (n+1)
Tree = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    Tree[x].append(y)
    Tree[y].append(x)

def bfs(start):
    q = []
    q.append(start)
    while q:
        start = q.pop(0)
        for i in Tree[start]:
            if check[i] == 0:
                check[i] += check[start] + 1
                q.append(i)


bfs(target1)

# def dfs(start):
#     for i in Tree[start]:
#         if check[i] == 0:
#             check[i] = check[start] + 1
#             dfs(i)

# dfs(target1)
if check[target2] == 0:
    print("-1")
else:
    print(check[target2])


# import sys
# input = sys.stdin.readline
# n = int(input())
# people = [0] * (n+1)

# target1, target2 = map(int, input().split())

# Tree = [[] for _ in range(n+1)]
# m = int(input())
# for i in range(m):
#     x, y = map(int, input().split())
#     Tree[x].append(y)
#     Tree[y].append(x)

# length = 0
# mask = 0
# people[target1] = 1
# cnt = [0] * (n+1)

# def dfs(start, end, tree):
#     global length, mask

#     length += 1
#     for i in tree[start]:
#         if i == end:
#             mask = 1
#             cnt[i] = length
#             return
        
#         else:
#             if people[i] == 0:
#                 people[i] = 1
#                 dfs(i, end, tree)
#                 length -= 1
#             cnt[i] = length
            

# dfs(target1, target2, Tree)

# if mask == 1:
#     print(cnt[target2])
# else:
#     print("-1")