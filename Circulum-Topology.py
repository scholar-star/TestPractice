from collections import deque
import copy

v = int(input())
indegree = [0]*(v+1)
# 진입차수

graph = [[] for i in range(v+1)]
# 간선 정보 입력 리스트

time = [0]*(v+1)

# 모든 간선 정보 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1 # 현재 과목에 진입차수 1
        graph[x].append(i) # 선수과목을 시작지점으로 함

# 위상정렬
def topology_sort():
    result = copy.deepcopy(time) # time(강의 시간 그래프) 완전 복사
    q = deque()

    for i in range(1,v+1): # 진입차수가 0인 노드를 우선 queue에 삽입
        if(indegree[i] == 0):
            q.append(i) # 시작지점

    while q:
        now = q.popleft()
        for i in graph[now]:
            # 해당 원소와 연결된 노드 진입차수 -= 1
            result[i] = max(result[i], result[now]+time[i])
            # 하나씩 선수과목들의 시간을 비교하며 큰 쪽을 최종값으로 함
            # 선수과목 시간 + 현재시간 > 현재시간
            indegree[i] -= 1
            if(indegree[i] == 0):
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()