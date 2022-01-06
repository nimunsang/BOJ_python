#다시 #이분탐색 #매개변수탐색
"""
https://www.acmicpc.net/problem/2110
[2110] : 공유기 설치
"""

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

def BinarySearch(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        current = arr[0]

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                cnt +=1 
                current = arr[i]
            
        if cnt >= C:
            global answer
            answer = mid
            start = mid+1
            
        else:
            end = mid-1
            
answer = 0
BinarySearch(arr, 1, arr[-1]-arr[0])
print(answer)