#해결 #다이나믹프로그래밍

"""
https://www.acmicpc.net/problem/2156
[2156] : 포도주 시식
"""

n = int(input())
lst = [0]
for i in range(n):
    lst.append(int(input()))

dp = [0]
dp.append(lst[1])

if n > 1:
    dp.append(lst[1] + lst[2])

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i]))
print(dp[n])