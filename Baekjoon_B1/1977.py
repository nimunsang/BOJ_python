M = int(input())
N = int(input())

i = 1
lst = []
while i**2 <= N:
    if i**2 in range(M, N+1):
        lst.append(i**2)
    i += 1

if len(lst) == 0: print(-1)
else:
    print(sum(lst))
    print(min(lst))

# =========첫 번째 풀이===========
# from math import *

# M = int(input())
# N = int(input())

# su_lst = []

# for i in range(int(sqrt(N))+1):
#     su_lst.append(i**2)

# my_lst = []
# for i in range(M, N+1):
#     if i in su_lst: my_lst.append(i)

# if len(my_lst) == 0: print(-1)
# else:
#     print(sum(my_lst))
#     print(min(my_lst))

