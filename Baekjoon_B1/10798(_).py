lst = []
for i in range(5):
    lst.append(list(input()))

for i in range(max(len(s) for s in lst)):
    for j in range(5):
        if i < len(lst[j]):
            print(lst[j][i], end = "")

# ===========내 처음 풀이============
# lst = []
# for i in range(5):
    # lst.append(list(input()))

# max_len = 0
# for i in range(5):
#     if len(lst[i]) > max_len: max_len = len(lst[i])

# for i in range(5):
#     while len(lst[i]) <= max_len:
#         lst[i] += " "

# a = 0
# while a != max_len :
#     for i in range(5):
#         if lst[i][a] == " ":
#             continue
#         print(lst[i][a], end = "")
#     a += 1