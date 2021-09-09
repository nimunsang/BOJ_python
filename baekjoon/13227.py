
# 내 풀이
# A, B = input().split()
# print(int(A)*int(B))
#맞긴 맞는데 시간이 너무오래걸림

#인터넷 풀이
# a, b = map(int, input().split())
# print(a*b)
#이것도 맞긴 맞는데 시간이 너무오래걸림. 내풀이랑 똑같은거
#a, b의 값을 map을 이용하는 것을 습관들이자

# 인터넷 풀이
from decimal import *
getcontext().prec = 600000

a, b = map(Decimal, input().split())
print(a*b)
#훨씬 빠르다