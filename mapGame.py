dx = [-1,0,1,0]
dy = [0,-1,0,1]

n,m =  tuple(map(int, input().split()))
r,c,d = tuple(map(int, input().split())) # *r,c는 0,0 기준 좌표*

visited = [[0 for i in range(m)] for j in range(n)] # 방문좌표
print(visited)
visited[r][c] = 1

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def left():
    global d # 전역변수 사용
    d = (d+1)%4

count = 1
turntimes = 0
while True:
    left()
    nx = r + dx[d]
    ny = c + dy[d]
    if(board[nx][ny]==0 and visited[nx][ny]==0): # 육지이고 방문 X
        board[nx][ny] = 1
        r = nx
        c = ny
        count+=1
        turntimes = 0
        continue
    else:
        turntimes += 1

    if(turntimes == 4):
        nx = r - dx[d]
        ny = c - dy[d]
        if(board[nx][ny] == 0):
            r = nx
            c = ny
        else:
            break
        turntimes = 0

print(count)

# "캐릭터가 육지에서 시작한다"라는 명제를 보지 못한 것이 큰 패착으로 작용했다.
# (1,1)이 아닌 (0,0)이 왼쪽 모서리임을 이해하지 못했다.

