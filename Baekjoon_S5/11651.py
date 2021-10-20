import sys
input = sys.stdin.readline
lst = []

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort(key= lambda x: (x[1], x[0]))

for x, y in lst:
    print(x, y)