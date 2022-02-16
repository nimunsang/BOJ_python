# https://www.acmicpc.net/problem/1302

N = int(input())
arr = [input() for _ in range(N)]

dic = dict()

for i in range(N):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

cnt = sorted(dic.items(), key=lambda x:x[1], reverse = True)[0][1]

ans = []
for key, value in dic.items():
    if value == cnt:
        ans.append(key)

ans.sort()
print(ans[0])

