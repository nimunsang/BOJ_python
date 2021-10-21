# =========내 풀이============
X = int(input())

lst = [1, 2, 4, 8, 16, 32, 64]

for i in range(len(lst)):
    if lst[i] > X:
        lst = lst[:i]
        break

cnt = 0
while True:
    if X == 0:
        print(cnt)
        break
    if lst[-1] > X:
        lst = lst[:-1]

    else:
        X -= lst[-1]
        cnt += 1

# """
# 인터넷 풀이(이진법으로 접근)
# """

# X = int(input())
# cnt = 0
# while X != 0:
#     if X%2 == 1:
#         cnt += 1
#     X //= 2
# print(cnt)
