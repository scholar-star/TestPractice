import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n,m,c = map(int, input().split())

# 단방향
cities = [False]*(n+1)
least_distances = [INF]*(n+1)

# 다익스트라
graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

cities[c] = True

def dijkstra(start): # 함수화
    h = []
    heapq.heappush(h, (start, 0)) # 시작 노드
    least_distances[start] = 0 # start 지점의 거리를 0
    while h:
        des, dis = heapq.heappop(h) # 목적지, 이전 길이
        if(least_distances[des] < dis): # 현재 distance보다 거리가 작으면
            continue

        for d in graph[des]: # 인접한 노드들(des, d[0], d[1]) - s,d,w
            cost = dis + d[1] # 인접한 노드의 길이를 같이 더해서 cost가 됨.(이전+현재) - 거쳐서 가기.
        # least_distances[des] = dis
        # if(graph[des]!=[]):
        #     for b in graph[des]:
        #         heapq.heappush(h,b)
            if cost < least_distances[d[0]]: # cost가 목적지까지 본래 최소값보다 작으면
                least_distances[d[0]] = cost # 갱신
                heapq.heappush(h, (d[0], cost)) # 목적지를 다음 노드로 하고 집어넣음


        # cities[des] = True
        # 나중 과정에서 count

dijkstra(c)
max_distance = max([l for l in least_distances if (l!=INF)])
print(len([le for le in least_distances if le!=INF])-1, max_distance)
#print(sum(cities)-cities[c], max([l for l in least_distances if (l!=INF)]))





