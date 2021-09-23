N = int(input())

for i in range(N):
    for j in range(N-i-1):
        print(" ", end = "")
    for k in range(2*i+1):
        print("*", end = "")
    print("")

for ii in range(N-1):
    for jj in range(ii+1):
        print(" ", end = "")
    for kk in range(2*(N-1-ii)-1):
        print("*", end = "")
    print("")

