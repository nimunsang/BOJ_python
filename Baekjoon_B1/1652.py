N = int(input())

lst = []
for i in range(N):
    lst.append(input())

cnt = 0
for i in range(N):
    mask = 0
    for j in range(1, len(lst[i])):
        if mask == 0 and lst[i][j] == "." and lst[i][j-1] == ".": 
            mask = 1
            cnt += 1
        elif lst[i][j] == "X": mask = 0

new_lst = []
for i in range(N):
    s = ""
    for j in range(N):
        s += lst[j][i]
    new_lst.append(s)

n_mask = 0
n_cnt = 0
for i in range(N):
    n_mask = 0
    for j in range(1, len(new_lst[i])):
        if n_mask == 0 and new_lst[i][j] == "." and new_lst[i][j-1] == ".": 
            n_mask = 1
            n_cnt += 1
        elif new_lst[i][j] == "X": n_mask = 0
        
print(cnt, n_cnt, end = " ")

# ========첫 번째 시도=============
# N = int(input())

# lst = []
# for i in range(N):
#     lst.append(input())

# r_cnt = 0
# l_cnt = 0
# for i in range(N):
#     if ("..X" in lst[i]): r_cnt += 1
#     if ("X.." in lst[i]): r_cnt += 1
#     if N >= 2 and ("X" not in lst[i]): r_cnt += 1

# new_lst = []
# for i in range(N):
#     s = ""
#     for j in range(N):
#         s += lst[j][i]
#     new_lst.append(s)

# for i in range(N):
#     if ("..X" in new_lst[i]): l_cnt += 1
#     if ("X.." in new_lst[i]): l_cnt += 1
#     if N >= 2 and ("X" not in new_lst[i]): l_cnt += 1
# print(r_cnt, l_cnt, end = " ") 
