import sys
input = sys.stdin.readline

S = input().strip()
N = S.count('()')
S = S.replace('()', '-')

line = 0
result = 0
for i in S:
    if i == '(':
        line += 1
    elif i == '-':
        result += line
    elif i == ')':
        line -= 1
        result += 1

print(result)