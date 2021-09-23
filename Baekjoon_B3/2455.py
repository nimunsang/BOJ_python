import sys

lst = []
sum = 0

for i in range(4):
    off, on = map(int, sys.stdin.readline().split())
    sum -= off
    lst.append(sum)
    sum += on
    lst.append(sum)

print(max(lst))


