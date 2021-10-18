M = int(input())
N = int(input())
    
lst = []
for i in range(M, N+1):
    if i == 1:
        pass
    elif i == 2:
        lst.append(i)
    else:
        mask = 1
        for j in range(2, i):
            if i%j == 0: 
                mask = 0
                break
        if mask == 1: lst.append(i)

if len(lst) == 0: print("-1")
else:
    print(sum(lst))
    print(min(lst))


# ===========함수 이용 깔끔========
# M = int(input())
# N = int(input())

# def is_sosu(a):
#     mask = 1
#     if a == 1: mask = 0
#     elif a == 2: mask = 1
#     else:
#         for i in range(2, a):
#             if a%i == 0: mask = 0
#     return mask
    
# lst = []
# for i in range(M, N+1):
#     if is_sosu(i): lst.append(i)

# if len(lst) == 0: print("-1")
# else:
#     print(sum(lst))
#     print(min(lst))