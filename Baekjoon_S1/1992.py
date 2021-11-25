#다시 # 답이 아님
# N = int(input())
N = 8
tree = [list(map(int, input())) for _ in range(N)]

def sep(n):
    temp = n//2
    if temp == 0:
        return

    for i in range(0, n, temp):
        for j in range(0, n, temp):
            t = [row[j:j+temp] for row in tree[i:i+temp]]
            l = []
            for k in t:
                l.extend(k)

            if 1 not in l:
                print("0", end = "")

            elif 0 not in l:
                print("1", end = "")
            
            else:
                print("(", end = "")
                sep(n//2)
                print(")", end = "")

sep(N)
