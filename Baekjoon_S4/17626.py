#30분 #다이나믹프로그래밍 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/17626
[17626] : Four Squares
"""

import math

n = int(input())

dp = [4] * (n+1)
dp[0] = 0
dp[1] = 1

k = 1
while k**2 <= n:
    dp[k**2] = 1
    k += 1

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])

print(dp[n])


"""
내 풀이
n = int(input())
dp = [4] * 50001

for i in range(1, 225):
    for j in range(1, i+1):
        for k in range(1, j+1):
            if i**2 + j**2 + k**2 > 50000:
                break

            dp[i**2 + j**2 + k**2] = 3

for i in range(1, 225):
    for j in range(1, i+1):
        if i**2 + j**2 > 50000:
            break

        dp[i**2 + j**2] = 2

for i in range(1, 225):
    if i**2 > 50000:
        break

    dp[i**2] = 1

print(dp[n])"""