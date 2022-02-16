arr = [(i+1, int(input())) for i in range(8)]
arr.sort(key = lambda x: x[1], reverse = True)
s, ans = 0, []
for i in range(5):
    s += arr[i][1]
    ans.append(arr[i][0])

print(s)
print(*sorted(ans))
