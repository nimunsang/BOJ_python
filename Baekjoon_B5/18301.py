import math

A, B, C = map(int, input().split())

print(math.floor((A+1)*(B+1)/(C+1))-1)