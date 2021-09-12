N = int(input())
T = []
for i in range(N):
    T.append(float(input()))
    T[i] = T[i] * 0.8

for i in range(N):
    print("${0:.2f}".format(T[i]))