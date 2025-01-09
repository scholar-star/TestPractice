from collections import deque

n,m = tuple(map(int, input().split()))
mazing = [list(map(int, input())) for _ in range(n)]

# def dfs(i,j):
#     global distance
#     if(i<0 or i>n-1 or j<0 or j>m-1):
#         return
#
#
#     if(mazing[i][j]==1):
#         mazing[i][j] = 2
#         dfs(i+1, j)
#         dfs(i, j+1)
#         dfs(i-1, j)
#         dfs(i, j-1)
#         distance+=1
#     return
# 최단 경로의 경우 bfs가 유리(모든 Node를 탐색하기 때문에)
def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue: # queue가 빌 때까지 반복
        x,y = queue.popleft()
        actions = [(ac[0], ac[1]) for ac in [(-1,0),(1,0),(0,-1),(0,1)]
                   if(x+ac[0]>=0 and x+ac[0]<=n-1 and y+ac[1]>=0 and y+ac[1]<=m-1)]
        for a in actions:
            nx = x + a[0] # 후보군들이라 임시로 지정
            ny = y + a[1]
            if(mazing[nx][ny]==0):
                continue
            if(mazing[nx][ny]==1):# 방문 안한 곳(방문한 곳은 최단거리로 채워지기 때문(1은 아님))
                mazing[nx][ny] = mazing[x][y]+1
                queue.append((nx,ny))

    return mazing[n-1][m-1]

print(bfs(0,0))

