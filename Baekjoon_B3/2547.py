import sys

T = int(input())

for i in range(T):
    q = input()
    sum = 0
    cnt = 0
    N = int(input())
    for j in range(N):
        candy = int(sys.stdin.readline())
        cnt += 1
        sum += candy

    if cnt >= 1:
        if sum % cnt == 0:
            print("YES")
        else:
            print("NO")

