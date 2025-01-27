n = int(input())
board = []
s=0

dr = [-1,0,1,0]
dc = [0,1,0,-1]

teachers = []

for i in range(n):
    l = input().split()
    s += l.count('S')
    for j in range(len(l)):
        if l[j] == 'T':
            teachers.append((i,j))
    board.append(l)
print(teachers)

# DFS
def dfs(i,j, board):
    if(i>=0 and i<n and j>=0 and j<n):
        if(board[i][j]=='X' or board[i][j]=='S'):
            board[i][j]='T'
        dfs(i+1,j,board)
        dfs(i-1, j, board)
        dfs(i, j+1, board)
        dfs(i, j-1, board)
    else:
        return

for i in range(n):
    for j in range(n):
        if(len(teachers)>0):
            r,c = teachers[0][0],teachers[0][1]
            if(i==r and j==c):
                dfs(i,j, board)
                print(board)
                teachers.pop(0)

print(board)