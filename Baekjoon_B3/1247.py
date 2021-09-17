# =======시간초과==============
# lst = []
# for i in range(3):
#     lst.append(int(input()))
#     sum = 0
#     for j in range(lst[i]):
#         sum += int(input())
#     if sum == 0: print("0")
#     elif sum > 0: print("+")
#     else: print("-")

#input을 사용하면 시간 초과 발생!
#반복문에서의 입력은... sys.stdin.readline()을 이용하기

import sys
for i in range(3):
    x = int(sys.stdin.readline())
    sum = 0
    for j in range(x):
        num = int(sys.stdin.readline())
        sum += num
    if sum == 0: print("0")
    elif sum > 0: print("+")
    else: print("-")
    