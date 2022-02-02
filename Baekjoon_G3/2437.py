#다시 #그리디알고리즘
"""
https://www.acmicpc.net/problem/2437
[2437] : 저울
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer =0 

for i in range(N):
    if answer + 1 >= arr[i]:
        answer += arr[i]
    else:
        break

print(answer+1)