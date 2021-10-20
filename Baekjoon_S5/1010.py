from math import *

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    if M-N < N: N = M-N

    res = factorial(M) // (factorial(N)*factorial(M-N))
    print(res)

# ============combination 이용==========
# from math import *

# T = int(input())

# for i in range(T):
#     N, M = map(int, input().split())
#     print(comb(M, N))

