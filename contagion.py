n,k = map(int, input().split())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

s,x,y = map(int, input().split())

dr = [-1,0,1,0]
dc = [0,1,0,-1]

last = [(0,0) for _ in range(k)]
# 깊이 우선 탐색
def dfs(i,j,kind):
    for _ in range(4):
        ni = dr[_]+i
        nj = dc[_]+j
        if(ni >= 0 and ni<n and nj>=0 and nj<n):
            if(l[ni][nj]==0):
                l[ni][nj] = kind
                last[kind-1] = (ni,nj)

for v in range(1, k+1):
    for i in range(n):
        for j in range(n):
            if(l[i][j]==v):
                last[v-1]=(i,j)

for _ in range(s):
    for v in range(1, k+1):
        dfs(last[v-1][0], last[v-1][1], v)

print(l[x-1][y-1])