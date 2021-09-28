A, B = map(int, input().split())
C, D = map(int, input().split())

lst = []
lst.append(A/C + B/D)
for i in range(3):
    A, B, C, D = C, A, D, B
    lst.append(A/C + B/D)

print(lst.index(max(lst)))
