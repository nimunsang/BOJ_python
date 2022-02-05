#해결 #백트래킹
"""
https://www.acmicpc.net/problem/2580
[2580] : 스도쿠
"""

arr = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

def checkrow(y, a):
    for i in range(9):
        if arr[y][i] == a:
            return False
    return True

def checkcol(x, a):
    for i in range(9):
        if arr[i][x] == a:
            return False
    return True
    
def checksq(y, x, a):
    y //= 3
    x //= 3
    for i in range(y*3, y*3+3):
        for j in range(x*3, x*3+3):
            if arr[i][j] == a:
                return False
    
    return True

def dfs(idx):
    if len(blank) == idx:
        for i in range(9):
            print(*arr[i])
        exit(0)
    
    for i in range(1, 10):
        x = blank[idx][1]
        y = blank[idx][0]

        if checkrow(y, i) and checkcol(x, i) and checksq(y, x, i):
            arr[y][x] = i
            dfs(idx+1)
            arr[y][x] = 0

dfs(0)