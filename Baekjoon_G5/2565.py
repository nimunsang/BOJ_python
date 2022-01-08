from itertools import combinations
N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()
lst = []  
for i in range(N):
    lst.append(arr[i][1])
print(lst)
dp = [0]*(N)

def descending(arr):
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            return False
    return True


while True:
    dp = []
    for i in range(len(arr)):
        cnt = 0
        for j in range(i+1, len(arr)):
            if arr[i]<arr[j]:
                cnt += 1
        dp.append(cnt)

    i = 1
    while True:
        try:
            if dp[i] > dp[i-1]:
                dp.pop(i)
            i += 1
        except:
            break
    
    print(dp)
    if descending(dp):
        break

print(dp)