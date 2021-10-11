T = int(input())

for i in range(T):
    lst = input().split()
    for j in lst:
        print(j[::-1], end = " ")
    print()