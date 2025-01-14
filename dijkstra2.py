import heapq
# heap
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)] # k번째를 시작점으로 한 간선의 도착점, 간선길이
distance = [INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    # q에 heap 적용하여 (0, start)를 넣음
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q) # 우선순위 최소 큐(default)
        if distance[now] < dist:
            continue
            # 이미 최단 거리로 정했으면 무시

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0])) #최단 거리, 도착점

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])