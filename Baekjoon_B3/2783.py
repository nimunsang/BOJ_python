import sys

a, b = map(int, input().split())
T = int(input())
x, y, z = [a], [b], [a*1000/b]
for i in range(T):
    p, q = map(int, sys.stdin.readline().split())
    x.append(p)
    y.append(q)
    z.append(p*1000/q)

print(round(min(z), 2))