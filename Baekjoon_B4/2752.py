K = list(map(int, input().split()))

for i in range(2):
    for j in range(i+1,3):
        if(K[i] > K[j]):
            tmp = K[i]
            K[i] = K[j]
            K[j] = tmp

for i in list(K):
    print(i, end=" ")