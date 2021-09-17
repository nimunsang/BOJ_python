import sys

M = int(input())
kong = 1

for i in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    if X == kong:
        kong = Y
    elif Y == kong:
        kong = X

print(kong)