#7분 #그리디알고리즘 #정렬
"""
https://www.acmicpc.net/problem/11399
[11399] : ATM
"""
N = int(input())
lst = list(map(int, input().split()))

lst.sort()
sum_arr = [0] * (N+1)

sum = 0
for i in range(1, N+1):
    sum += lst[i-1]
    sum_arr[i] += sum_arr[i-1] + sum

print(sum_arr[N])