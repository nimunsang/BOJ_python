# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
numbers = [i for i in range(N, 0, -1)]
stack = []
answer = []
i = 0
while numbers:
    stack.append(numbers.pop())
    answer.append('+')
    while stack and stack[-1] == arr[i]:
        stack.pop()
        answer.append('-')
        i += 1

if i == N:
    for ans in answer:
        print(ans)
else:
    print("NO")