from collections import deque

n,k = map(int, input().split())

l = []
data = [] # 바이러스 정보 리스트(나중에 queue로 사용)
# "너비우선 탐색"
# : 1번 할 때마다 "여러 갈래"로 퍼져나감

# 깊이우선이면은 한 갈래를 쭉 타고 내려가는 것에 적합.
for i in range(n):
    l.append(list(map(int, input().split())))
    for j in range(n):
        if l[i][j]!=0:
            data.append((l[i][j], 0, i, j)) # 바이러스 종류, 시간, x, y

data.sort() # 바이러스 번호 오름차순대로 정렬
q = deque(data)

s,x,y = map(int, input().split())

dr = [-1,0,1,0]
dc = [0,1,0,-1]

# queue가 동날 때까지 너비우선
while q:
    v,sec,row,col = q.popleft()
    if sec==s:
        break
    # 원래 풀었던 아이디어와 유사
    for i in range(4):
        ni = row+dr[i]
        nj = col+dc[i]
        if 0<=ni<n and 0<=nj<n:
            if(l[ni][nj]==0):
                l[ni][nj]=v
                q.append((v,sec+1, ni,nj))

print(l[x-1][y-1])
