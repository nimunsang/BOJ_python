#해결 #자료구조 #스택
"""
https://www.acmicpc.net/problem/1918
[1918] : 후위 표기식
"""

import sys
input = sys.stdin.readline

S = list(input().rstrip())
priority = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}
stack = []
answer = ""

for char in S:
    if char.isalpha():
        answer += char

    elif char == '(':
        stack.append(char)
    
    elif char == ')':
        while True:
            v = stack.pop()
            if v == '(':
                break

            answer += v
    
    else:
        while stack and priority[char] <= priority[stack[-1]]:
            answer += stack.pop()
        stack.append(char)

while stack:
    answer += stack.pop()

print(answer)