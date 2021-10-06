import sys
input = sys.stdin.readline

while True:
    s = input().rstrip('\n')
    if s == 'END':
        break
    print(s[::-1])

# while True:
#     s = input()
#     if s == 'END':
#         break
#     print(s[::-1])