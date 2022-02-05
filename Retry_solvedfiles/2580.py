arr = [list(map(int, input().split())) for _ in range(9)]

def check(y, x, target):
    for i in range(9):
        if arr[y][i] == target:
            return False
    
    for i in range(9):
        if arr[i][x] == target:
            return False
    
    for i in range(y//3*3, y//3*3+3):
        for j in range(x//3*3, x//3*3+3):
            if arr[i][j] == target:
                return False
    
    return True

def dfs(idx):
    if idx == LENGTH:
        for a in arr:
            print(*a)
        exit(0)

    y = blank[idx][0]
    x = blank[idx][1]
    for i in range(1, 10):
        if check(y, x, i):
            arr[y][x] = i
            dfs(idx+1)
            arr[y][x] = 0

blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

LENGTH = len(blank)
dfs(0)