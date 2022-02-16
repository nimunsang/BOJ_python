#다시 #자료구조 #스택 #연결리스트
"""
https://www.acmicpc.net/problem/1406
[1406] : 에디터
"""

import sys
input = sys.stdin.readline

S = list(input().rstrip())
M = int(input())
stack1, stack2 = [], []
for a in S:
    stack1.append(a)

for _ in range(M):
    op = list(input().rstrip().split())
    if op[0] == 'L' and stack1:
        stack2.append(stack1.pop())

    elif op[0] == 'D' and stack2:
        stack1.append(stack2.pop())

    elif op[0] == 'B' and stack1:
        stack1.pop()

    elif op[0] == 'P':
        stack1.append(op[1])

print(''.join(stack1) + ''.join(reversed(stack2)))








