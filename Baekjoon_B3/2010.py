import sys
N = int(input())

sum = 0
for i in range(N):
    num = int(sys.stdin.readline())
    sum += num-1

print(sum+1)
