import sys
input = sys.stdin.readline

cnt = 0
for i in range(8):
    s = input()
    for j in range(8):
        if (s[j] == 'F') and \
        ((i%2 == 0 and j%2==0) or (i%2 == 1 and j%2==1)) : cnt+= 1
print(cnt)