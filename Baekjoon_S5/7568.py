N = int(input())

x_lst = []
y_lst = []

for i in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

rank_lst = [1]*N
for i in range(N):
    for j in range(N):
        if x_lst[i]>x_lst[j] and y_lst[i]>y_lst[j]:
                rank_lst[j] += 1
        
for i in range(N):
    print(rank_lst[i], end = " ")