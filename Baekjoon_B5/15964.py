def mine(A, B):
    return (A+B)*(A-B)

A, B = map(int, input().split())

print(mine(A, B))

# A, B = map(int, input().split())
# print((A+B)*(A-B))