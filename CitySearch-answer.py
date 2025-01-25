from collections import deque

n,m,k,x = map(int, input().split())
roads = [[] for _ in range(n+1)] # 도시에 연결된 또 다른 도시들
for i in range(m):
    a,b = map(int, input().split())
    roads[a].append(b)

# 다익스트라
# 정확히 말하면 BFS로서 해결 가능

lens = [-1 for _ in range(n+1)] # 방문 안한 도시를 -1로 표기
lens[x] = 0

starts = deque([x])

while starts:
    start = starts.popleft()
    for road in roads[start]:
        if lens[road] == -1: # 아직 방문하지 않았다면
            lens[road] = lens[start] + 1 # 스타트 + 1
            starts.append(road)
        # 방문했다면 다른 곳에서 direct로 갔단 뜻 - 최단 거리 갱신 불필요

l = []
for i in range(n+1):
    if(k==lens[i]):
        l.append(i)

if l!=[]:
    for i in l:
        print(i, end=' ')
else:
    print(-1)





