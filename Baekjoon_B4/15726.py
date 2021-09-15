from math import *

A, B, C = map(int, input().split())

print(max(A*B//C, floor(A/B*C)))