# https://www.acmicpc.net/problem/1918

S = input()

stack = []
superior = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}

for a in S:
    if a.isalpha():
        print(a, end="")
    else:
        if a == '(':
            stack.append(a)

        elif a == ')':
            while stack[-1] != '(':
                print(stack.pop(), end="")
            stack.pop()

        else:
            while stack and stack[-1] != '(' and superior[stack[-1]] >= superior[a]:
                print(stack.pop(), end="")

            stack.append(a)

while stack:
    print(stack.pop(), end="")
