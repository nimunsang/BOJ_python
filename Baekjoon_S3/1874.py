#해결 #자료구조 #스택
"""
https://www.acmicpc.net/problem/1874
[1874] : 스택 수열
"""

import sys
input = sys.stdin.readline

N = int(input())
s = []
op = []
cnt = 0
mask = 1
for i in range(N):
    num = int(input())
    while cnt < num:
        cnt += 1
        op.append('+')
        s.append(cnt)
    
    if s[-1] == num:
        s.pop()
        op.append('-')
    
    else:
        mask = -1
    
if mask == -1:
    print("NO")
else:
    for i in op:
        print(i)