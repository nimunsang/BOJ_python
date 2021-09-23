import sys

N = int(input())
lst = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    sum = 0
    if len(set(a)) == 1:
        sum += (10000 + a[0]*1000)
    elif len(set(a)) == 2:
        if a[0] == a[1]:
            sum += 1000 + a[0]*100
        elif a[0] == a[2]:
            sum += 1000 + a[0]*100
        else:
            sum += 1000 + a[1]*100
    else:
        sum += max(a) * 100
    lst.append(sum)

print(max(lst))
    