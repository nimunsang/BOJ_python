#다시 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/16637
[16637] : 괄호 추가하기
"""

N = int(input())
S = input()
op, num = [], []

for a in S:
    if a.isdigit():
        num.append(a)
    else:
        op.append(a)


def solve(idx, subtotal):
    global answer
    if idx == len(op):
        answer = max(answer, int(subtotal))
        return

    solve(idx+1, str(eval(subtotal + op[idx] + num[idx+1])))

    if idx+1 < len(op):
        solve(idx+2, str(eval(subtotal + op[idx] + str(eval(num[idx+1] + op[idx+1] + num[idx+2])))))


answer = 0
solve(0, num[0])

print(answer)