import sys

INF = int(1e9)
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
# 2차원 배열 : [[a]*n for _ in range(n)]
# 한번 더 확인

for i in range(n+1):
    for j in range(n+1):
        if (i == j):
            graph[i][j] = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    # 양방향 가능

x,k = map(int, input().split())

# for i in range(1, n+1):
#     graph[1][i] = min(graph[1][i], graph[1][i]+graph[i][k]+graph[k][x],
#                       graph[1][k]+graph[k][i]+graph[i][x])
# 본래 플로이드 워셜 수행(그곳에서 1로 시작하고 k를 거친 뒤, x에 다다르는 것만 구함)

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

# 최소 + 최소 = 최소
# 1에서 k까지 최소, k에서 x까지 최소
distance = graph[1][k]+graph[k][x]

if(distance >= INF):
    print(-1)
else:
    print(distance)