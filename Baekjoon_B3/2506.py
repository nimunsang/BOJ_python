import sys

N = int(input())

sum = 0
lst = []

a = list(map(int, sys.stdin.readline().split()))

for i in a:
    if i == 1:
        sum += 1
    else:
        lst.append(sum)
        sum = 0
lst.append(sum)

result = 0
for i in lst:
    result += i*(i+1)//2

print(result)