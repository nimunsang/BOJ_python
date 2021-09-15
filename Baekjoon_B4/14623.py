B1 = int(input())
B2 = int(input())

sum_B1 = 0
sum_B2 = 0
def toDec(N, sum):
    cnt = 0
    while(N != 0):
        if N%10 == 1:
           sum += 2**cnt
           N = N // 10
           cnt += 1
        else:
            N = N // 10
            cnt += 1
    return sum
dec_B1 = toDec(B1, sum_B1)
dec_B2 = toDec(B2, sum_B2)
result = dec_B1 * dec_B2

cnt = 0
sum = []
while(result != 0):
    if(result % 2 == 1):
        sum.append(1)
        result = result // 2
    else:
        sum.append(0) 
        result = result // 2

for i in range(1, len(sum)+1):
    print(sum[len(sum)-i], end="")

