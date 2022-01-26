#해결 #분할정복 #재귀
"""
https://www.acmicpc.net/problem/1780
[1780] : 종이의 개수
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = {-1: 0, 0: 0, 1: 0}

def check(y, x, n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != arr[y][x]:
                return False
    return True

def cut(y, x, n):
    if check(y, x, n):
        ans[arr[y][x]] += 1
        return

    for i in range(y, y+n, n//3):
        for j in range(x, x+n, n//3):
            cut(i, j, n//3)
                
cut(0, 0, N)
for value in ans.values():
    print(value)