import sys
input = sys.stdin.readline

N = int(input())

s = 0
for i in range(1, N+1):
    s += (N//i) * i

print(s)
