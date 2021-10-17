lst = list(map(int, input().split()))
mylst = []

def GCD(a, b):
    if b%a == 0:
        return a
    else:
        return GCD(b%a, a)

def LSM(a, b):
    return a*b//GCD(a, b)

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            l = []
            l.append(lst[i])
            l.append(lst[j])
            l.append(lst[k])
            mylst.append(l)

lsm_lst = []
for i in range(len(mylst)):
    l = LSM(LSM(mylst[i][0], mylst[i][1]), mylst[i][2])
    lsm_lst.append(l)

print(min(lsm_lst))

# ===========첫 번째 풀이============
# lst = list(map(int, input().split()))

# mylst = []
# for i in range(3):
#     for j in range(i+1, 4):
#         for k in range(j+1, 5):
#             su = max(lst[i], lst[j], lst[k])
#             while True:
#                 if (su%lst[i] == 0) and (su%lst[j] == 0) and (su%lst[k] == 0):
#                     mylst.append(su)
#                     break
#                 su += 1
# print(min(mylst))


# ============두 번째 풀이===========
# lst = list(map(int, input().split()))
# m = min(lst)

# while True:
#     cnt = 0
#     for i in lst:
#         if m%i==0: cnt += 1
#     if cnt >= 3:
#         mask = 1
#         print(m)
#         break
#     m += 1