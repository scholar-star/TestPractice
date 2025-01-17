
n = int(input())

graph = [[] for _ in range(n+1)]
ltimes = [0]

for i in range(1, n+1):
    t = tuple(map(int, input().split()))
    time = t[0]
    ltimes.append(time)
    first = t[1:len(t)-1]
    if(first!=()):
        for f in first:
            graph[i].append(f)

mintimes = [0 for _ in range(n+1)]

for i in range(1,n+1):
    if graph[i]==[]:
        mintimes[i] = ltimes[i]
    else:
        mintimes[i] = max([mintimes[j] for j in graph[i]])+ltimes[i]
    print(mintimes[i])

