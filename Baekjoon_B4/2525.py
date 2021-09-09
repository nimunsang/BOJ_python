A, B= map(int, input().split())
C = int(input())

if(C/60 >= 1):
    A += int(C/60)
    C = C % 60

if(B+C >= 60):
    A += 1
    B = B + C - 60
else:
    B += C

if(A >= 24):
    A -= 24
print("{0} {1}".format(A, B))