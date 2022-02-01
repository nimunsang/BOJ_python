N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for i in range(1, N+1):
    inp = list(map(int, input().split()))
    cost = inp[0]
    lst = inp[1:-1]
    for l in lst:
        graph[i].append(l)
        indegree[l] += 1
    
print(graph)
print(indegree)
    