#해결 #다이나믹프로그래밍 #배낭문제
"""
https://www.acmicpc.net/problem/12865
[12865] : 평범한 배낭
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0, 0]]
for i in range(N):
    bag.append(list(map(int, input().split())))
    
ans = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = bag[i]
        if j < W:
            ans[i][j] = ans[i-1][j] 
         
        else:
            ans[i][j] = max(ans[i-1][j], ans[i-1][j-W] + V)

print(ans[N][K])