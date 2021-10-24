#50분 #자료구조 #스택 #문자열
"""
https://www.acmicpc.net/problem/4949
[4949] : 균형잡힌 세상
"""

import sys
input = sys.stdin.readline

def sol(s):
    sum_s, sum_m = 0, 0
    lst = []
    for i in s:
        if i == '(' :
            sum_s += 1
            lst.append(i)
        elif i == ')':
            sum_s -= 1
            lst.append(i)
        elif i == '[':
            sum_m += 1
            lst.append(i)
        elif i == ']':
            sum_m -= 1
            lst.append(i)
        if sum_s < 0 or sum_m < 0:
            return -1
    if sum_s > 0 or sum_m > 0 :
        return -1
    elif len(lst) == 0:
        return 1
    elif sum_s == 0 and sum_m == 0:
        i = 1
        while True:
            if len(lst) == 0:
                return 1
            if lst[i] == ']':
                if lst[i-1] == '[':
                    lst.pop(i)
                    lst.pop(i-1)
                    i -= 1
                elif lst[i-1] == '(':
                    return -1
            elif lst[i] == ')':
                if lst[i-1] == '(':
                    lst.pop(i)
                    lst.pop(i-1)
                    i -= 1
                elif lst[i-1] == '[':
                    return -1
            else:
                i += 1
while True:
    s = input().rstrip()
    if s == '.':
        break
    elif sol(s) == 1:
        print("yes")
    elif sol(s) == -1:
        print("no")