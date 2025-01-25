n,m = map(int, input().split())
board = []
temp = [[0]*m for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))

result = 0 # 안전 영역 수

dr = [-1,0,1,0]
dc = [0,1,0,-1]

# DFS
def propagation(i, j):
    # if(i<0 or i>=n or j<0 or j>=m):
    #     return;
    # else:
    #     board[i][j]=2
    #     propagation(board, i-1, j)
    #     propagation(board, i+1, j)
    #     propagation(board, i, j-1)
    #     propagation(board, i, j+1)
    # 상하좌우 좌표 우선 구하기
    for k in range(4): # 상하좌우에 대해
        ni = i+dr[k] # 인덱스
        nj = j+dc[k]
        if (ni>=0 and ni<n and nj>=0 and nj<m): #조건 만족시
            if(temp[ni][nj]==0):
                temp[ni][nj]=2 # 바이러스 배치
                propagation(ni, nj) # 갱신한 좌표에 대해 실행(재귀)
        # 불만족 시 실행 안함

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 벽 3개 세우는 경우의 수 + "계산"
def calc(count):
    global result # result 사용
    if count == 3: # 벽이 3개 다 세워졌으면
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    propagation(i, j)

        result = max(result, get_score())
        return
    # 울타리 경우의 수
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                count += 1
                calc(count) # 3될때까지 재귀
                board[i][j] = 0 # 다시 복구
                count -= 1

calc(0)
print(result)

