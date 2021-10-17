num = set(range(1, 10001))
gen_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gen_num.add(i)

self_num = sorted(num - gen_num)

for i in self_num:
    print(i)

# ===========내 두번째 풀이===========
# lst = [i for i in range(1, 10001)]

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     if i in lst:
#         lst.remove(i)

# for i in lst:
#     print(i)