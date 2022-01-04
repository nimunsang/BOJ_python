#30분 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/14891
[14891] : 톱니바퀴
"""

from collections import deque

def checkleft(num, r):
    if num == 0 or gear[num][6] == gear[num-1][2]:
        return
    
    else:
        checkleft(num-1, -r)
        gear[num-1].rotate(-r)

def checkright(num, r):
    if num == 3 or gear[num][2] == gear[num+1][6]:
        return
    
    else:
        checkright(num+1, -r)
        gear[num+1].rotate(-r)

gear = [deque(map(int, input())) for _ in range(4)]
K = int(input())
for i in range(K):
    num, direction = map(int, input().split())
    checkleft(num-1, direction)
    checkright(num-1, direction)
    gear[num-1].rotate(direction)

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2**i

print(answer)       