#2시간30분 #구현 #정렬
"""
https://www.acmicpc.net/problem/2108
[2108 : 통계학]
최빈값 구현이 결국 문제였는데,
인터넷을 찾아보니 counter의 most_common()을 사용하여
다들 문제를 풀었다.....
결국 원리는 dict을 만드는건데 나는 절댓값 4000을 보고, 
하나하나 dict을 만들어 풀었다.(시간이 그래도 적게 걸릴것이라 판단)
다음부터는 counter를 써야겠다!억울하네.....
"""

import sys
input = sys.stdin.readline

#lst에 -4000~4000, 그 빈도를 저장한다(절댓값이 4000이라 크지않음)
N = int(input())
lst = [[i-4000, 0] for i in range(8001)]

sum_input = 0
for i in range(N):
    a = int(input())
    lst[a+4000][1] += 1
    sum_input += a

#정렬
new_lst = []
for i in range(8001):
    if lst[i][1] != 0:
        new_lst.append(lst[i])

#중간값
lst = []
for i in range(len(new_lst)):
    for j in range(new_lst[i][1]):
        lst.append(new_lst[i][0])
middle = lst[N//2]

#최대, 최솟값
max_lst = new_lst[-1][0]
min_lst = new_lst[0][0]

#최빈값
new_lst.sort(key = lambda x: x[1], reverse= True)
if N == 1:
    most = new_lst[0][0]
else:  
    if new_lst[0][1] == new_lst[1][1]:
        most = new_lst[1][0]
    else:
        most = new_lst[0][0]

#1
print(round(sum_input/N))
#2
print(middle)
#3
print(most)
#4
print(max_lst - min_lst)