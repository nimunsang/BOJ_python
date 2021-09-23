import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

sum_a = 0
sum_b = 0
mask = 0
for i in range(10):
    if A[i] > B[i]:
        sum_a += 3
        mask = 1
    elif A[i] == B[i]:
        sum_a += 1
        sum_b += 1
    else:
        sum_b += 3
        mask = 2
    
print("{0} {1}".format(sum_a, sum_b))

if mask == 0:
    print("D")
elif sum_a == sum_b:
    for i in range(10):
        sum_a -= A[9-i]
        sum_b -= B[9-i]
        if sum_a < sum_b:
            print("A")
            break
        elif sum_a > sum_b:
            print("B")
            break
elif sum_a > sum_b:
    print("A")
else:
    print("B")