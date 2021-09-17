A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())

if A1 == A2:
    print("0")
elif((A1<A2) & (((B1 == B2)&(C1 <= C2)) | (B1<B2))):
    print(A2-A1)
else:
    print(A2-A1-1)
    
print(A2-A1+1)
print(A2-A1)
