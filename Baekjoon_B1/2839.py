import sys
input = sys.stdin.readline

N = int(input())

cnt =0 
min_cnt = N
tmp = N//3
lst = []
for i in range(tmp+1):
    for j in range(tmp+1):
        num = 5*i+3*j
        if num == N:
            cnt = i+j
            if min_cnt > cnt : min_cnt = cnt

if cnt == 0 : print("-1")
else: print(min_cnt)

# ==============두번째 풀이======
# N = int(input())

# cnt = 0
# while True:
#     if N%5 == 0:
#         cnt += N//5
#         print(cnt)
#         break
#     N -= 3
#     cnt += 1
#     if N < 0: 
#         print("-1")
#         break