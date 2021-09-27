import sys

N = []
mask = 0
for i in range(7):
    num = int(sys.stdin.readline())
    N.append(num)
    if N[i] % 2 == 1:
        mask = 1

if mask == 0:
    print("-1")
else:
    even = []
    sum = 0
    for i in N:
        if i%2 == 1:
            even.append(i)
            sum += i
    print(sum)
    print(min(even))