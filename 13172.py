
arr = []
while True:
    try:
        N = int(input())
        arr.append(N)
    except:
        break


length = len(arr)
firstroot = arr[0]
roots = [[0]*2 for _ in range(length)]
for i in range(1, length):
    if arr[i-1] > arr[i]:
        roots[i-1][0] = arr[i]
    
    else:
        k = i-1
        while k >= 0 and arr[i] > arr[k]:
            k -= 1
        roots[k+1][1] = arr[i]

for root in roots:
    print(root)

