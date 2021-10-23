"""
https://www.acmicpc.net/problem/10815
[10815] : 숫자 카드
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def BinarySearch(start, end, lst, x):
    if start > end :
        return 0
    else:
        mid = (start + end) // 2
        if x == lst[mid]:
            return 1
        elif x > lst[mid]:
            return BinarySearch(mid+1, end, lst, x)
        else:
            return BinarySearch(start, mid-1, lst, x)

for i in B:
    if BinarySearch(0, N-1, A, i) == 1:
        print("1", end = " ")
    else:
        print("0", end = " ")