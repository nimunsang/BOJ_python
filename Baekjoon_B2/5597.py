import sys
input = sys.stdin.readline

s = [i for i in range(1, 31)]
for i in range(28):
    s.remove(int(input()))

print(min(s))
print(max(s))