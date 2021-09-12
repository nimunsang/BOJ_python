L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if(A%C ==0):
    finish_A = A//C
else:
    finish_A = A//C + 1

if(B%D == 0):
    finish_B = B//D
else:
    finish_B = B//D + 1

print(L - max(finish_A, finish_B))