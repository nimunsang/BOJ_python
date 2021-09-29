import sys

N = int(input())

c, nc = 0, 0
for i in range(N):
    a = int(sys.stdin.readline())
    if a == 1: c += 1
    else: nc += 1

if c > nc:
    print("Junhee is cute!")
elif nc > c:
    print("Junhee is not cute!")