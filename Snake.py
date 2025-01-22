n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

k = int(input())
for _ in range(k):
    r,c = map(int, input().split())
    board[r][c] = 2

l = int(input())
ts = []
for _ in range(l):
    time, d = input().split()
    time = int(time)
    ts.append((time,d))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

head = (0,0) # 행,열

dir = 0
i = 0
# while(head[0] >= 0 and head[0]<n and head[1]>=0 and head[1]<n):
#     if (head[0]+dx[dir%4] >= n and head[0]+dy[dir%4] < n):
#         break
#
#     if (board[head[0]+dx[dir%4]][head[1]+dy[dir%4]]==1):
#         break
#
#     head = (head[0]+dx[dir%4],head[1]+dy[dir%4])
#     print(head)
#     if(board[head[0]][head[1]]==2):
#         board[head[0]][head[1]] = 1
#     else:
#         board[tail[0]][tail[1]] = 0
#
#     if (i in [t[0] for t in ts]):
#         print(i)
#         for t in ts:
#             if(t[1]=='D'):
#                 dir += 1
#             if(t[1]=='L'):
#                 dir -= 1
#         ts.pop(ts.index(t))
#
#     i += 1
# 사과가 있을 경우 꼬리를 머리가 나아간 만큼 떼어내야 하기에, 꼬리를 리스트에 담아두면 좋다.

index = 0 # 시간 감소
x,y=head
board[x][y] = 1
tail = [(x,y)]
while True:
    nx = x+dx[dir%4]
    ny = y+dy[dir%4] # 나아간 값
    print(nx, ny)
    if(0<=nx and nx<n and 0<=ny and ny<n and board[nx][ny]!=1):
        if(board[nx][ny]==0):
            # 없을 경우 이전 꼬리(1칸당 기록했던 것 중 최근 것)은 잘라내야함
            # 사과 없음
            board[nx][ny] = 1
            tail.append((nx, ny))  # 저장
            px, py = tail.pop(0)
            board[px][py] = 0
        if(board[nx][ny]==2):
            board[nx][ny] = 1
            tail.append((nx, ny))
    else:
        i += 1
        break
    x,y = nx, ny # 머리의 이동(방향만큼 1칸 이동) - 새로운 머리
    i += 1
    if index<l and i==ts[index][0]:
        if(ts[index][1]=='L'):
            dir -= 1
        if(ts[index][1]=='D'):
            dir += 1
        index += 1

print(i)
