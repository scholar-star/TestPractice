import sys
input = sys.stdin.readline
# 함수를 변수화, 간략화
INF = int(1e9)
# 무한 == 1억

n,m = tuple(map(int, input().split()))
#노드, 간선
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 2차원 리스트 만들기
graph = [[] for i in range(n+1)]
visited = [False]*(n+1) # 방문 노드 리스트
distance = [INF]*(n+1) # 노드 최단거리 리스트

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a를 시작으로하는 노드의 도착점과 길이

def get_smallest_node(): # 방문하지 않은 노드 중, 최단거리 노드 반환
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        # 도착점, 거리
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가는 최단거리
for i in range(1,n+1):
    if distance[i]==INF:
        print("NOT REACH")
    else:
        print(distance[i])
