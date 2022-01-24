#30분 #분할정복 #재귀
"""
https://www.acmicpc.net/problem/2448
[2448] : 별 찍기-11
"""

N = int(input())
arr = [[" "] *(N*2) for _ in range(N)]

def drawsmall(y, x):
    arr[y][x] = '*'
    arr[y+1][x-1] = '*'
    arr[y+1][x+1] = '*'
    for i in range(5):
        arr[y+2][x-2+i] = '*'

def draw(y, x, n):
    if n == 3:
        drawsmall(y, x)
        return
    
    draw(y, x, n//2)
    draw(y+n//2, x-n//2, n//2)
    draw(y+n//2, x+n//2, n//2)

draw(0, N-1, N)

for a in arr:
    print(''.join(a))