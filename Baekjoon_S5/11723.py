import sys
input = sys.stdin.readline

S = []
M = int(input())
for i in range(M):
    command = input().rstrip()
    if command == 'all':
        S = [i for i in range(1, 21)]
    elif command == 'empty':
        S = []
    else:
        a, b = command.split(' ')
        b = int(b)
        if (a == 'add') and (b not in S):
            S.append(b)
        elif (a == 'remove') and (b in S):
            S.remove(b)
        elif a == 'check':
            if b in S:
                print("1")
            else:
                print("0")
        elif a == 'toggle':
            if b in S:
                S.remove(b)
            else:
                S.append(b)


# ============set 활용===============
# import sys
# input = sys.stdin.readline

# S = set()
# M = int(input())
# for i in range(M):
#     command = input().rstrip()
#     if command == 'all':
#         S = set([i for i in range(1, 21)])
#     elif command == 'empty':
#         S = set()
#     else:
#         a, b = command.split(' ')
#         b = int(b)
#         if a == 'add': S.add(b)
#         elif a == 'remove': S.discard(b)
#         elif a == 'check':
#             if b in S: print("1")
#             else: print("0")
#         elif a == 'toggle':
#             if b in S: S.discard(b)
#             else: S.add(b)
