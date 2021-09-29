N = int(input())

for i in range(1, N+1):
    cnt = 0
    for j in range(N-i):
        print(" ", end = "")
    while cnt != i:
        print("* ", end = "")
        cnt += 1
    print("")