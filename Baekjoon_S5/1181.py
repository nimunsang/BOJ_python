import sys
input = sys.stdin.readline

N = int(input())

s_set = set()
for i in range(N):
    s = input().rstrip()
    s_set.add(s)

s_lst = list(s_set)
s_lst.sort()
s_lst.sort(key=len)
# s_lst.sort(key= lambda x: (len(x), x))

for i in s_lst:
    print(i)