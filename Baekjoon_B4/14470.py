A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0
if(A < 0):
    time += abs(A) * C + D
    time += B * E

else:
    time += (B-A) * E
print(time)