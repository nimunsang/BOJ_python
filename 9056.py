while True:
    N = int(input())
    if N == -1: break

    lst = []
    for i in range(1, N):
        if N % i == 0:
            lst.append(i)
    
    if sum(lst) == N:
        print(str(N) + " = " + ' + '.join((str(i) for i in lst)))
    else:
        print("{0} is NOT perfect.".format(N))

# ================처음풀이=============
# from math import *

# N = int(input())

# def yak_lst(num):
#     lst = []
#     for i in range(1, int(sqrt(num))+2):
#         if i not in lst and num % i == 0:
#             lst.append(i)
#             if num//i not in lst:
#                 lst.append(num//i)
#     lst.sort()
#     lst.remove(num)
#     return lst
    
# def wan_print(num):
#     print("{0} = 1".format(num), end = "")
#     for i in range(1, len(yak_lst(num))):
#         print(" + ", end = "")
#         print(yak_lst(num)[i], end = "")
#     print("")

# while N != -1:
#     if sum(yak_lst(N)) == N:
#         wan_print(N)
#     else:
#         print("{0} is NOT perfect.".format(N))
#     N = int(input())