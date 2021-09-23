import sys

for i in range(3):
    zero = 0
    one = 0
    a = list(map(int, sys.stdin.readline().split()))
    zero = a.count(0)
    one = a.count(1)

    if (zero == 1) & (one == 3):
        print("A")
    elif (zero == 2) & (one == 2):
        print("B")
    elif (zero == 3) & (one == 1):
        print("C")
    elif (zero == 4) & (one == 0):
        print("D")
    else:
        print("E")