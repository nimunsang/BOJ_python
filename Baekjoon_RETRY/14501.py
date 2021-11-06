#다시
N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

for i in range(N):
    if lst[N-i-1][0] > i+1:
        lst[N-i-1] = [0, 0]   

dp = [0] * 16

for i in range(N-1, -1, -1):
    dp[i] = max(dp[i+1], dp[i + lst[i][0]] + lst[i][1])

print(dp)