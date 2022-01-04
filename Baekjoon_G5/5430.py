#30분 #구현 #자료구조 #문자열 #파싱 #덱
"""
https://www.acmicpc.net/problem/5430
[5430] : AC
"""

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    if n == 0:
        arr = deque([])
    elif ',' not in arr:
        arr = deque([int(arr[1:-1])])
    else:
        arr = deque(map(int, arr[1:-1].split(',')))
    
    r = 0
    for i in range(len(p)):
        if p[i] == 'R':
            r += 1
        else:
            if r % 2 == 0:
                try:
                    arr.popleft()
                except:
                    print("error")
                    break
            elif r % 2 == 1:
                try:
                    arr.pop()
                except:
                    print("error")
                    break
    else:
        if r%2 == 1:
            arr.reverse()

        s = '[' + ','.join(map(str, arr)) + ']'
        print(s)