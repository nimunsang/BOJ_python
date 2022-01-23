import sys
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input())
    
    for i in range(E):
        u, v = map(int, input().split())