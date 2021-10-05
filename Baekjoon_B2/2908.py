# A, B = map(str, input().split())
# s_a = ""
# s_b = ""
# for i in range(1, len(str(A))+1):
#     s_a += str(A)[len(str(A))-i]
#     s_b += str(B)[len(str(B))-i]

# print(max(int(s_a), int(s_b)))

A, B = map(str, input().split())
A = int(A[::-1])
B = int(B[::-1])

print(max(A, B))