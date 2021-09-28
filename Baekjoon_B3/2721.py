import sys

T = int(input())

for i in range(T):
    sum = 0
    num = int(sys.stdin.readline())
    for j in range(1, num+1):
        sum += (j*(j+1)*(j+2))//2

    print(sum)