import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*10001

for i in range(N):
    a = int(input())
    lst[a] += 1

for i in range(10001):
    for j in range(lst[i]):
        print(i)