import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        sum = 2
        for i in range(len(str(N))):
            if str(N)[i] == '1':
                sum += 2
            elif str(N)[i] == '0':
                sum += 4
            else:
                sum += 3
        sum += len(str(N)) - 1
        print(sum)