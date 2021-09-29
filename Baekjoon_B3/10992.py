N = int(input())

for i in range(1, N):
    if i==1:
        for j in range(N-i):
            print(" ", end = "")
        print("*")
    else:
        for j in range(N-i):
            print(" ", end = "")
        print("*", end = "")
        for k in range(2*i-3):
            print(" ", end = "")
        print("*")
    
for i in range(2*N-1):
    print("*", end = "")