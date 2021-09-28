A = list(map(int, input().split()))

h = min(A)
A.remove(h)
A.remove(min(A))
w = min(A)

print(h*w)