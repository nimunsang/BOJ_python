#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/2565
[2565] : 전깃줄
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: x[0])
arr = list(map(lambda x: x[1], arr))

print(arr)
dp = [0] * (N)
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    
    dp[i] += 1

print(dp)
print(N-max(dp))