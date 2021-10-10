x, y = map(int, input().split())

lst_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lst_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
cnt = 0
for i in range(x-1):
    cnt += lst_month[i]

cnt += y
print(lst_day[cnt%7])

# ===========첫 번째 풀이===========
# x, y = map(int, input().split())

# lst_31 = [1, 3, 5, 7, 8, 10, 12]
# lst_30 = [4, 6, 9, 11]
# lst_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
# cnt = 0
# for i in range(x):
#     if i in lst_31: cnt += 31
#     elif i in lst_30: cnt += 30
#     else: cnt += 28

# cnt += y
# print(lst_day[cnt%7])