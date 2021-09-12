N = []
sum = 0
for i in range(5):
    N.append(int(input()))
    if(N[i] < 40):
        N[i] = 40
    sum += N[i]
print(sum//5)
