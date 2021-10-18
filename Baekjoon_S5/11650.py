import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort()

for x, y in lst:
    print(x, y)