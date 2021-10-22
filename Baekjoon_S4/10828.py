"""
https://www.acmicpc.net/problem/10828
[10828] : 스택
"""

import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    command = input().rstrip()
    if command == 'pop':
        if len(lst) == 0:
            print("-1")
        else:    
            print(lst.pop(-1))
    elif command == 'size':
        print(len(lst))
    elif command == 'empty':
        if len(lst) == 0:
            print("1")
        else:
            print("0")
    elif command == 'top':
        if len(lst) == 0:
            print("-1")
        else:
            print(lst[-1])
    else:
        a, b = command.split(' ')
        lst.append(b)