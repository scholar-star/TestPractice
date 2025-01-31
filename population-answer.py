# 연합의 정의가 중심 국가에서 인접한 것만 포함하는 것은 아니고,
# 그 너머까지도 포함할 수 있는 것이었음
from collections import deque

n,l,r = map(int, input().split())

populations = []
for _ in range(n):
    populations.append(list(map(int, input().split())))

dr = [-1,0,1,0]
dc = [0,1,0,-1]

result = 0

def bfs(x, y, index):
    united = []
    # 연결된 연합 정보를 일시적으로 담음
    united.append((x, y))

    q = deque([])
    q.append((x, y))

    union[x][y]=index # 현재 연합 식별 번호
    summary = populations[x][y] # 현재 연합의 전체 인구수가 될 것임
    count = 1 # 연합 국가 수

    while q:
        x,y = q.popleft()
        for _ in range(4):
            nr = dr[_]+x
            nc = dc[_]+y
            if (0<=nr<n and 0<=nc<n and union[nr][nc]==-1):
                if l<=abs(populations[nr][nc]-populations[x][y])<=r:
                    q.append((nr, nc))
                    union[nr][nc] = index
                    summary += populations[nr][nc]
                    count += 1
                    united.append((nr, nc))

    for o,p in united:
        populations[o][p] = summary // count

total_count = 0
# 더 이상 인구 이동을 못할 때까지 반복
# index : 0 ~ n*n-1번까지
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if (union[i][j]==-1):
                bfs(i, j, index)
                index += 1

    if index == n*n:
        break
    total_count += 1

print(total_count)
