A, B, C = map(int, input().split())

D = int(input())

if (D/3600) >= 1:
    A += D//3600
    D %= 3600
    
if (D/60) >= 1:
    B += D//60
    D %= 60

C += D
if (C>=60):
    B += 1
    C -= 60

if (B>=60):
    A += 1
    B -= 60

A %= 24
print("{0} {1} {2}".format(A, B, C))