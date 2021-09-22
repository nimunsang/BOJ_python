A, B = map(int, input().split())

tmp1 = min(A, B)
tmp2 = max(A, B)
A = tmp1
B = tmp2
if (B-A+1) % 2 == 0:
    print((B+A)*((B-A+1)//2))
else:
    print((B+A) * ((B-A+1)//2) + (B+A)//2)