# ===============내 풀이===============
N = int(input())

first = 0
last = 0
lst = []
while True:
    if str(first)[len(str(first))-3:] == "666":
        num = str(first)  + str(last).zfill(3)
        last += 1
        if last % (10**3) == 0:
            first += 1
            last = 0
    elif str(first)[len(str(first))-2:] == "66":
        num = str(first) + "6" + str(last).zfill(2)
        last += 1
        if last % (10**2) == 0:
            first += 1
            last = 0
    elif str(first)[len(str(first))-1:] == "6":
        num = str(first) + "66" + str(last).zfill(1)
        last += 1
        if last % (10**1) == 0:
            first += 1
            last = 0
    else:
        if first == 0: num = "666"
        else:
            num = str(first) + "666"  
        first += 1 
    lst.append(num)

    if len(lst) == N: break

print(lst[-1])

# ==============인터넷 풀이===========
# 밑 방법처럼 하면 시간이 너무 많이 걸릴거같았음...
# 실제로 내 방법보다 10배 오래걸림ㅋㅋ
# N = int(input())
# s = "666"
# num = 666
# cnt = 0
# while True:
#     if s in str(num):
#         cnt += 1
    
#     if cnt == N:
#         print(num)
#         break
#     num += 1