N, M, K = map(int, input().split())

max = 0
if(M >= N-M): # O가 더 많을 때
    max = K + K-M
else:
    max = N-K + N - M

print(max)