import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    k = int(input())
    lst.append(k)

for i in sorted(lst):
    print(i)