p, k = map(int, input().split())

a = 0
b = 0
for i in range(2,k):
    if (p % i == 0):
        a = i
        b = p//i
        break

if (a == 0) & (b == 0):
    print("GOOD")
else:
    print("BAD {0}".format(min(a, b)))
