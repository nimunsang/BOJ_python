#다시 #분할정복 #재귀
"""
https://www.acmicpc.net/problem/1780
[1780] : 종이의 개수
"""

import sys
input = sys.stdin.readline

def cut(a, b, n):
    mask = lst[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if lst[i][j] != mask:
                for k in range(3):
                    for l in range(3):
                        cut(a + k * n//3, b + l * n//3, n//3)
                return

    if mask == -1:
        count[0] += 1
    elif mask == 0:
        count[1] += 1 
    else:
        count[2] += 1


N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

count = [0, 0, 0]
cut(0, 0, N)

for i in count:
    print(i)