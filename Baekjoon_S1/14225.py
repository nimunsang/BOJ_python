#10분 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/14225
[14225] : 부분수열의 합
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(N):
    if ans+1 < arr[i]:
        break
    else:
        ans += arr[i]

print(ans+1)
