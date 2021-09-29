import sys

N = int(input())

sum = 0
for i in range(N):
    stu, app = map(int, sys.stdin.readline().split())
    sum += app%stu

print(sum)