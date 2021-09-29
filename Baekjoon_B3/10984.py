import sys

T = int(input())
for i in range(T):
    N = int(input())
    GPA = 0
    sum_c = 0
    for j in range(N):
        C, G = map(float, sys.stdin.readline().split())
        GPA += C*G
        sum_c += C
    GPA /= sum_c
    print("{0} {1: .1f}".format(int(sum_c), GPA))
