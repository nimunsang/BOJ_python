"""
https://www.acmicpc.net/problem/10845
[10845] : 큐
"""

import sys
input = sys.stdin.readline

N = int(input())

queue = []
for i in range(N):
    command = input().rstrip()
    if command == 'pop':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])    
            queue.pop(0)
        
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif command == 'front':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
    else:
        a, b = command.split(' ')
        queue.append(int(b))