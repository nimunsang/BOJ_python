def dfs(depth, v):
    if depth == 6:
        print(*lst)
    else:
        for i in range(v, length):
            if not visited[i]:
                lst[depth] = s[i]
                visited[i] = 1
                dfs(depth+1, i+1)
                visited[i] = 0


while True:
    s = input()
    if s == '0':
        break
    else:
        length = int(s[0])
        visited = [0] * (length)
        s = list(map(int, s.split()))[1:]
        lst = [0] * 6
        dfs(0, 0)
        print()