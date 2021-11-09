#25분 #수학 #문자열 #그리디알고리즘
"""
https://www.acmicpc.net/problem/1541
[1541] : 잃어버린 괄호
"""
s = input()

lst = s.split('-')

for i in range(len(lst)):
    lsum = 0
    if '+' in lst[i]:
        l = map(int, lst[i].split('+'))
        lsum = sum(l)
        lst[i] = lsum

    lst[i] = int(lst[i])

result = lst[0]
if len(lst) > 1:
    for i in range(1, len(lst)):
        result -= lst[i]

print(result)