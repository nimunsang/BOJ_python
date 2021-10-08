l1 = list(map(str, input()))
l2 = list(map(str, input()))
first_l2 = len(l2)
same_lst = []
for i in l1:
    if i in l2:
        same_lst.append(i)
        l2.remove(i)
print(len(l1) + first_l2 - len(same_lst)*2)

# ------인터넷풀이
# a = input()
# b = input()
# res = 0
# for i in range(97, 123):
#     res += abs(a.count(chr(i)) - b.count(chr(i)))
# print(res)