N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end = "")
    for k in range(2*(N-i)-1):
        print("*", end = "")
    print("")
for ii in range(N-1):
    for l in range(N-ii-2):
        print(" ", end = "")
    for m in range(2*(ii+1)+1):
        print("*", end = "")
    print("")