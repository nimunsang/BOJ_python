# sort의 key를 활용한 풀이
n = int(input())

for i in range(n):
    players = []
    p = int(input())
    for j in range(p):
        c, name = input().split()
        c = int(c)
        players.append((c, name))
    
    players.sort(key= lambda player: player[0])
    print(players[-1][1])


# =============dictonary를 활용한 풀이==========
# n = int(input())

# for i in range(n):
#     p = int(input())

#     dic = dict()
#     for j in range(p):
#         c, name = input().split()
#         c = int(c)
#         dic[name] = c

#     max_c = max(dic.values())

#     for k, v in dic.items():
#         if v == max_c:
#             print(k)



#
# ===========첫 번째 풀이===============
# n = int(input())

# for i in range(n):
#     p = int(input())
#     c_lst = []
#     name_lst = []
   
#     for j in range(p):
#         c, name = input().split()
#         c_lst.append(int(c))
#         name_lst.append(name)
#     print(name_lst[c_lst.index(max(c_lst))])



# =============두 번째 풀이===========
# n = int(input())

# for i in range(n):
#     p = int(input())
#     max = 0
#     mname = ""
   
#     for j in range(p):
#         c, name = input().split()
#         c = int(c)
#         if c > max: 
#             max = c
#             mname = name
    
#     print(mname)

