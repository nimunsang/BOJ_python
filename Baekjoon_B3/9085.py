import sys

T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int, sys.stdin.readline().split()))
    print(sum(lst))