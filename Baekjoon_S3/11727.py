#30분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/11727
[11727] : 2xn 타일링 2
"""

n = int(input())

arr = [0, 1]
for i in range(1, n):

    if i %2 == 0:
        arr.append(arr[i]*2-1)
    else:
        arr.append(arr[i]*2+1)

print(arr[-1] % 10007)
