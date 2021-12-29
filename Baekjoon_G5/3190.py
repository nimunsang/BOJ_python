#1시간 #구현 #자료구조 #시뮬레이션 #덱 #큐
"""
https://www.acmicpc.net/problem/3190
[3190] : 뱀
"""

from collections import deque
import sys
input = sys.stdin.readline

def play(board, direction):
    time = 0
    head = deque()
    head.append([1, 1])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ind = 0
    
    while True: 
            dir = [dy[ind], dx[ind]]

            time += 1
            nexty = head[-1][0]+dir[0]
            nextx = head[-1][1]+dir[1]

            if 1<=nexty<N+1 and 1<=nextx <N+1:
                if [nexty, nextx] in head:
                    return time
                
                else:
                    head.append([nexty, nextx])
            else:
                return time

            if board[head[-1][0]][head[-1][1]] == 1:
                board[head[-1][0]][head[-1][1]] = 0
            
            else:
                head.popleft()
            
            if len(direction) > 0 and time == direction[0][0]:
                if direction[0][1] == 'L':
                    ind = (ind-1)%4
                else:
                    ind = (ind+1)%4
                direction.popleft()
        
N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]

K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1

L = int(input())
direction = deque()
for _ in range(L):
    X, C = input().split()
    direction.append([int(X), C])

print(play(board, direction))