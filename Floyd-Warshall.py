INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
# 모든 간선의 길이를 나타내는 2차원 배열

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    # 시작, 도착, 길이
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1): # 노드 개수마다 진행
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            # 거쳐가는 것과 직선으로 가는 것 비교

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()