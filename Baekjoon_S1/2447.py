#해결 #분할정복 #재귀
"""
https://www.acmicpc.net/problem/2447
[2447] : 별 찍기 10
"""

N = int(input())

def empty(x, y, n, lst):
    if n == 3:
        lst[x+1][y+1] = " "
    
    else:
        tmp = n//3
        for i in range(x + tmp, x + 2*tmp):
            for j in range(y+tmp, y+2*tmp):
                lst[i][j] = " "
        for k in range(0, n, tmp):
            for l in range(0, n, tmp):
                empty(x+k, y+l, tmp, lst)

    
stars = [['*' for _ in range(N)] for _ in range(N)]

empty(0, 0, N, stars)

for i in range(N):
    print(''.join(stars[i]))