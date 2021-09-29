import sys
import math

T = int(input())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N%H == 0:
        a = H
        b = N//H
    else:
        a = N%H
        b = math.ceil(N/H)
    print(str(a) + str(b).zfill(2))