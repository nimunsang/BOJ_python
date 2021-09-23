N = int(input())

for i in range(N):
    for k in range(i):
        print(" ", end = "")
    for j in range(2*(N-i)-1):
        print("*", end = "")
    print("")
