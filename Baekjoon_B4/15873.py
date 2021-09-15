N = int(input())

if(N // 100 >= 1):
    if(N // 10 <= 10):
        A = 10
        B = N%100
    elif(N // 10 > 10):
        A = N//100
        B = 10
elif N == 1010:
    A = 10
    B = 10
else:
    A = N//10
    B = N%10

print(A+B)