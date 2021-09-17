A, B = map(int, input().split())

if (A%4 == 0) & (B%4 == 0):
    print(abs(B-A)//4)

elif(A%4 == 0):
    if B in range(A-3, A):
        print(A-B)
    else:
        Ax = A//4-1
        Bx = B//4
        Ay = 0
        By = 4 - B%4
        print(abs(Bx-Ax)+abs(By-Ay))

elif B%4 == 0:
    if A in range(B-3, B):
        print(B-A)
    else:
        Ax = A//4
        Bx = B//4 - 1
        Ay = 4 - A%4
        By = 0
        print(abs(Bx-Ax)+abs(By-Ay))

else:
    SN = abs(A%4 - B%4)
    EW = abs(B//4 - A//4)
    print(SN+EW)


