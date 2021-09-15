N = list(map(int, input().split()))

sum = N[0]
big = 0
small = 0
P = []
Q = []
for i in range(1, 4):
    P.append(N[0]+N[i]) # [11, 14, 24]
    sum += N[i] # sum = 41

for i in range(3):
    Q.append(abs(sum - P[i]*2))
    
print(min(Q))