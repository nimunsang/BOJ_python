# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()


def binarysearch(start, end):
    mid = (start+end)//2

    if start > end:
        print(mid)
        return

    cnt = 1
    s = arr[0]
    for i in range(1, N):
        if arr[i] >= s + mid:
            cnt += 1
            s = arr[i]

    if cnt >= C:
        binarysearch(mid+1, end)

    elif cnt < C:
        binarysearch(start, mid-1)


binarysearch(1, arr[-1]-1)