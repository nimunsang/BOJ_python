N, T, C, P = map(int, input().split())

if (N%T == 0):
    N = N - 1

print(N//T*C*P)
