from math import *

def f(N): 
    return factorial(N)

N, K = map(int, input().split())
print(f(N) // (f(K) * f(N-K)))