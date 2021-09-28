s = []

for i in range(5):
    l = list(map(int, input().split()))
    s.append(sum(l))

print("{0} {1}".format(s.index(max(s))+1, max(s)))