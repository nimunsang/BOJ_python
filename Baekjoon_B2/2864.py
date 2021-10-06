A, B = input().split()

# A_lst, B_lst = [], []

# if A.count('5') + A.count('6') == 0: A_lst.append(int(A))
# if B.count('5') + B.count('6') == 0: B_lst.append(int(B))

# for i in range(len(A)):
#     if A[i] == '5' or A[i] == '6':
#         A_lst.append(int(A.replace(A[i], '5')))
#         A_lst.append(int(A.replace(A[i], '6')))

# for i in range(len(B)):
#     if B[i] == '5' or B[i] == '6':
#         B_lst.append(int(B.replace(B[i], '5')))
#         B_lst.append(int(B.replace(B[i], '6')))

# print(min(A_lst) + min(B_lst), max(A_lst) + max(B_lst))

min = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min, max)