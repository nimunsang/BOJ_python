#다시 #자료구조 #스택
"""
https://www.acmicpc.net/problem/2493
[2493] : 탑
"""

N = int(input())
arr = list(map(int, input().split()))
s = []
ans = []

for i in range(N):
    while s:
        if s[-1][1] > arr[i]:
            ans.append(s[-1][0] + 1)
            break
    
        else:
            s.pop()
    
    if not s:
        ans.append(0)
    s.append([i, arr[i]])

print(*ans)