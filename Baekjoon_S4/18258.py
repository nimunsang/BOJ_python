#10분 #자료구조 #큐
"""
https://www.acmicpc.net/problem/18258
[18258] : 큐2
"""
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

deq = deque([])
for i in range(N):
    command = input().rstrip()
    if command == 'pop' :
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif command == 'front':
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    elif command == 'back':
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])
    else:
        a, b = command.split()
        deq.append(int(b))
