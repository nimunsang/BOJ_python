#8분..
"""
https://www.acmicpc.net/problem/10866
[10866] : 덱
"""

import sys
input = sys.stdin.readline

N = int(input())

deq = []
for i in range(N):
    command = input().rstrip()
    if command == 'pop_front':
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.pop(0))
    elif command == 'pop_back':
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.pop(-1))
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
    elif command.split()[0] == 'push_front':
        deq.insert(0, int(command.split()[1]))
    elif command.split()[0] == 'push_back':
        deq.append(int(command.split()[1]))