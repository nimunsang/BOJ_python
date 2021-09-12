S = list(map(int, input().split()))
T = list(map(int, input().split()))

S_sum = 0
T_sum = 0
for i in S:
    S_sum += i

for i in T:
    T_sum += i

print(max(S_sum, T_sum))

