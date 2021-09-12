lst = []
ans_in = []
ans = []
for i in range(3):
    N = list(map(int, input().split()))
    lst.append(N)
    for j in range(3):
        ans_in.append(lst[i][j+3] - lst[i][j])
    ans.append(ans_in)
    ans_in.clear()
print(ans)
        

