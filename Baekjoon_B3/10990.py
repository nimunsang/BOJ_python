N = int(input())

for i in range(1, N+1):
    j = N - i
    if i == 1:
        print(" "*j, "*", sep = '')
    else:
        print(" "*j, "*", " "*((2*i)-3), "*", sep = '')