N = int(input())

sum = 4
tmp = 0
for i in range(0, N):
    tmp = (2**i) * (2**i+1) * 2 + (2**i)**2
    sum += tmp
print(sum)