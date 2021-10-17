import sys
input = sys.stdin.readline

T = int(input())

def GCD(a, b):
    if b%a == 0:
        return a
    else:
        return GCD(b%a, a)

for i in range(T):
    a, b = map(int, input().split())
    if a > b: a, b = b, a

    print(a*b//GCD(a, b), GCD(a, b))