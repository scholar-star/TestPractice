from itertools import combinations # 조합 함수

n = int(input())
board = []
teachers = []
spaces = [] # 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j]=='T':
            teachers.append((i,j))

        if board[i][j]=='X':
            spaces.append((i,j))

def watch(x,y,direction): # 감시(이 것에 관해서는 재귀를 쓸 필요가 없음)
    if direction==0: # 왼쪽 방면 검사
        while y>=0:
            if board[x][y]=='S': # 길목에 학생이 있을 경우
                return True
            if board[x][y]=='O':
                return False
            y-=1
    if direction==1: # 오른쪽 방면 검사
        while y<n:
            if board[x][y]=='S': # 길목에 학생이 있을 경우
                return True
            if board[x][y]=='O':
                return False
            y+=1
    if direction==2: # 위쪽 방면 검사
        while x>=0:
            if board[x][y]=='S': # 길목에 학생이 있을 경우
                return True
            if board[x][y]=='O':
                return False
            x-=1
    if direction==3: # 아래쪽 방면 검사
        while x<n:
            if board[x][y]=='S': # 길목에 학생이 있을 경우
                return True
            if board[x][y]=='O':
                return False
            x+=1
    return False

def detecting():
    for x,y in teachers: # 선생 위치에 대해
        for i in range(4):
            if(watch(x,y,i)):
                return True
    return False

detect = False
for data in combinations(spaces, 3): # 빈 공간 중에서 3개를 고르는(장애물 위치 선정) 경우의 수
    # data : 3개 선정
    for x,y in data:
        board[x][y]='O'

    if not detecting():
        detect = True
        break

    for x,y in data:
        board[x][y]='X' # 다시 새 배치를 위한 원위치

if detect:
    print('YES')
else:
    print('NO')



