"""
https://www.acmicpc.net/problem/1292
[1292] : 쉽게 푸는 문제
"""

A, B = map(int, input().split())

lst = []
cnt = 0
for i in range(1, 46):
    for j in range(i):
        lst.append(i)
        cnt += 1
        if cnt == B: 
            break
    if cnt == B:
        break
lst = lst[A-1:]
print(sum(lst))


# ========인터넷 풀이 ==========
# A, B = map(int, input().split())

# lst = []
# for i in range(1, 46):
#     lst += [i]*i

# print(sum(lst[A-1:B]))