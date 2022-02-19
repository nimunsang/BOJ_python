#다시 #이분탐색 #가장긴증가하는부분순열:O(nlogn))
"""
https://www.acmicpc.net/problem/12015
[12015] : 가장 긴 증가하는 부분 순열
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in range(N):
    left = 0
    right = len(dp)-1

    while left <= right:
        mid = (left+right)//2

        if dp[mid] < arr[i]:
            left = mid+1
        else:
            right = mid-1

    if left >= len(dp):
        dp.append(arr[i])
    else:
        dp[left] = arr[i]

print(len(dp)-1)