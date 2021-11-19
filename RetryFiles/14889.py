#다시
from itertools import *

M = int(input())

C = combinations(range(M), M//2)
ran = list(range(M))
A = []
B = []
for i in C:
    A.append(i)
    B.append(ran - list(i))
print(A)
print(B)