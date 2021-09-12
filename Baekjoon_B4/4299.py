A, B = map(int, input().split())

if ((A+B)%2 != 0) | (A<B):
    print("-1")
else:
    C = (A+B)//2
    D = abs((A-B)//2)
    A = max(C, D)
    B = min(C, D)

    print("{0} {1}".format(A, B))