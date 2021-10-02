N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

chong_count = len(A)
bu_count = 0
A = [i-B for i in A]
for i in A:
    if i > 0:
        if i%C == 0: bu_count += i//C
        else: bu_count += i//C+1

print(chong_count + bu_count)