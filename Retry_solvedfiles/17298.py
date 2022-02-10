# https://www.acmicpc.net/problem/17298

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = deque()
stack = []
while arr:
    v = arr.pop()
    while stack and stack[-1] <= v:
        stack.pop()
    if len(stack) == 0:
        answer.appendleft(-1)
    else:
        answer.appendleft(stack[-1])
    stack.append(v) 
print(*answer)