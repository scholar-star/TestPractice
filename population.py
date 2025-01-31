import math

n,l,r = map(int, input().split())
populations = []

dr = [-1,0,1,0]
dc = [0,1,0,-1]

# DFS 결합?
# 중심 국가의 인접 + 전파
def immigration(pops, i, j):
    rot = 1
    tot = pops[i][j]
    for _ in range(4):
        nr = dr[_]+i
        nc = dc[_]+j
        if(0<=nr<n and 0<=nc<n):
            if(l<=abs(pops[i][j]-pops[nr][nc])<=r):
                rot+=1
                tot+=pops[nr][nc]
            else:
                continue

    print(tot)
    if(rot==1):
        return False

    div = math.trunc(tot/rot)
    pops[i][j] = div
    for _ in range(4):
        nr = dr[_]+i
        nc = dc[_]+j
        if(0<=nr<n and 0<=nc<n):
            pops[nr][nc] = div

    return True



for _ in range(n):
    populations.append(list(map(int, input().split())))

migrate = 0
for i in range(n):
    for j in range(n):
        if(immigration(populations, i, j)):
            migrate += 1

for i in range(n):
    for j in range(n):
        print(populations[i][j], end=" ")
    print()

print(migrate)
