import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1: a = 5000000
    elif 2<=a<=3: a = 3000000
    elif 4<=a<=6: a = 2000000
    elif 7<=a<=10: a = 500000
    elif 11<=a<=15: a = 300000
    elif 16<=a<=21: a = 100000
    else: a = 0

    if b==1: b = 5120000
    elif 2<=b<=3: b = 2560000
    elif 4<=b<=7: b = 1280000
    elif 8<=b<=15: b = 640000
    elif 16<=b<=31: b = 320000
    else: b = 0
    print(a+b)