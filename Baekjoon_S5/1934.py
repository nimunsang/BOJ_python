import sys
input = sys.stdin.readline

T = int(input())

def gcd(a, b):
    if b%a == 0:
        return a
    else:
        return gcd(b%a, a)

for i in range(T):
    a, b = map(int, input().split())
    if a > b: a, b = b, a
    print(a*b//gcd(a, b))

#===========함수 이용을 안하면..?========
#import sys
# input = sys.stdin.readline

# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     if a > b: a, b = b, a
    # c = a
    # d = b
    # while True:
    #     if d%c == 0:
    #         print(a*b//c)
    #         break
    #     else:
    #         e = d%c
    #         d = c
    #         c = e