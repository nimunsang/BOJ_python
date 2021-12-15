from collections import Counter

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
c = dict(Counter(stages))
print(c)

for a in sorted(c.items()):
    
print(sorted(c.items()))