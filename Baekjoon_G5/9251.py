#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/9251
[9251] : LCS
"""

s1 = input()
s2 = input()
l1 = len(s1) 
l2 = len(s2)
dp = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])


#     A C A Y K P
# C   0 1 1 1 1 1
# A   1 1 2 2 2 2
# P   1 1 2 2 2 3 
# C   1 2 2 2 2 2
# A   1 2 3 3 3 3
# K   1 2 3 3 4 4