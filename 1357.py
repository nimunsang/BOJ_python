X, Y = input().split()

Revx = int(X[::-1])
Revy = int(Y[::-1])

print(int(str(Revx+Revy)[::-1]))