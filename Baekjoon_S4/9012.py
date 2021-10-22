"""
https://www.acmicpc.net/problem/9012
[9012] : 괄호
"""

T = int(input())

def is_VPS(s):
    if s.count('(') != s.count(')'):
        return -1
    else:
        left_count = 0
        right_count = 0
        for i in range(len(s)):
            if s[i] == '(':
                left_count += 1
            else:
                right_count += 1

            if right_count > left_count: return -1
    return 1
    
for i in range(T):
    s = input()
    if is_VPS(s) == 1:
        print("YES")
    else:
        print("NO")