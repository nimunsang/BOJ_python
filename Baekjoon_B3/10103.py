T = int(input())

a_sum = b_sum = 100
for i in range(T):
    a, b = map(int, input().split())
    if a > b:
        b_sum -= a
    elif a < b:
        a_sum -= b

print(a_sum)
print(b_sum)