# ==============내 풀이============
N = int(input())

cnt = 0
for i in range(N):
    s = input()
    l = len(set(s))

    diff_cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]: 
            diff_cnt += 1
    
    if diff_cnt == l: cnt += 1

print(cnt)


# ============인터넷 풀이===========
# N = int(input())
# res = N

# for i in range(N):
#     s = input()
#     for j in range(1, len(s)):
#         if s[j] == s[j-1]:
#             pass
#         elif s[j-1] in s[j:]:
#             res -= 1
#             break

# print(res)