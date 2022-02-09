# https://www.acmicpc.net/problem/2493

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
ind = []
for i in range(N):
    if len(stack) == 0:
        print(0, end = " ")
    
    else:
        while stack and arr[i] > stack[-1]:
            ind.pop()
            stack.pop()
        if len(stack) == 0:
            print(0, end = " ")
        else:
            print(ind[-1], end = " ")

    ind.append(i+1)
    stack.append(arr[i])