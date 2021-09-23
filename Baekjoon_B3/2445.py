N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end = "")
    for k in range(2*(N-i-1)):
        print(" ", end = "")
    for l in range(i+1):
        print("*", end = "")
    print("")

for ii in range(N-1):
    for jj in range(N-ii-1):
        print("*", end = "")
    for kk in range(2*(ii+1)):
        print(" ", end = "")
    for ll in range(N-ii-1):
        print("*", end = "")
    print("")