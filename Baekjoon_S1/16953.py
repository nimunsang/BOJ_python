#1시간 #그래프이론 #그리디알고리즘 #그래프탐색 #BFS
"""
https://www.acmicpc.net/problem/16953
[16953] : A->B
"""

A, B = map(int, input().split())

from collections import deque

#BFS풀이
mask = 0
answer = 0
def bfs():
    global mask, answer
    q = deque()
    q.append((A, 1))
    while q:
        n, cnt = q.popleft()
        if n*2==B or n*10+1 == B:
            mask = 1
            answer = cnt+1
            break

        if n*2 <= B:
            q.append((n*2, cnt+1))
        if n*10+1 <= B:
            q.append((n*10+1, cnt+1))
bfs()
if mask == 1:
    print(answer)
else:
    print(-1)


#그냥 풀이
"""
cnt = 1
while A != B:
    if B == 0:
        break

    elif B%2 == 0:
        B //= 2

    elif B%10 == 1:
        B //= 10

    else:
        break

    cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)
"""
