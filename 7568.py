N = int(input())

x_lst = []
y_lst = []
for i in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

cnt_lst = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if x_lst[i]>x_lst[j] and y_lst[i]>y_lst[j]:
            cnt += 1
    cnt_lst.append(cnt)

rank = 1
r = 0
rank_lst = [0]*N
while True:
    m = max(cnt_lst)
    if m == -1: break
    cnt = cnt_lst.count(m)
    rank += r

    for i in range(cnt):
        rank_lst[cnt_lst.index(m)] += rank
        cnt_lst[cnt_lst.index(m)] = -1
    
    r = cnt
    
for i in rank_lst:
    print(i, end = " ")