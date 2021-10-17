N = int(input())
mylst = ["4", "7"]
lst = ["4", "7"]
mask = 0
while True:
    for s in lst:
        for n in mylst:
            lst.append(s+n)
        if int(s+n) >= 1000000:
            mask = 1
            break
    if mask == 1: break

lst = list(map(int, lst))
l = 0

for i in range(1, len(lst)):
    if N in range(lst[i-1], lst[i]):
        print(lst[i-1])
        l = 1
        break
    if l == 1: break
# ===============내 풀이가 길지만.. 훨씬 빠르당=======




# ==========인터넷 풀이=============
# n = int(input())
# while True:
#     flag = True
#     for i in str(n):
#         if i!="4" and i!="7":
#             flag = False
#             n -= 1
#     if flag :
#         print(n)
#         break