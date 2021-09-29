import sys

T = int(input())

for i in range(T):
    Y_sum, K_sum = 0, 0
    for j in range(9):
        Y, K = map(int, sys.stdin.readline().split())
        Y_sum += Y
        K_sum += K
    
    if Y_sum > K_sum: print("Yonsei")
    elif Y_sum < K_sum: print("Korea")
    else: print("Draw")