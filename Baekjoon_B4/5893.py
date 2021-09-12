N = int(input())

sum = 0
i = 0
while(N != 0):
    if N%2==1:
        sum = sum + pow(2, i)
        N = N//10
        i += 1
    else:
        N = N//10
        i += 1

sum *= 17

res = []

while sum != 0:
    if sum%2 == 1:
        res.append(1)
        sum = sum // 2
    else:
        res.append(0)
        sum = sum // 2

result = 0
for i in range(len(res)):
    result = result + res[i] * (10**i)
print(result)