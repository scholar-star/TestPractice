from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 이동 가능한 위치들 담음
    post = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dr = [-1, 0, 1, 0] # 상하좌우 이동
    dc = [0, 1, 0, -1]

    for i in range(4):
        next_1_x = pos1_x + dr[i]
        next_1_y = pos1_y + dc[i]
        next_2_x = pos2_x + dr[i]
        next_2_y = pos2_y + dc[i]
        if(board[next_1_x][next_1_y] == 0 and board[next_2_x][next_2_y] == 0): # 두 칸이 모두 비어있다면
            next_pos.append({(next_1_x, next_1_y), (next_2_x, next_2_y)})

        if pos1_x==pos2_x: # 로봇이 가로형태
            for i in [-1,1]: #위, 아래 회전
                if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0: # 위쪽 두 칸이 모두 비어있다면
                    next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                    next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
        elif pos1_y==pos2_y: # 로봇이 세로형태
            for i in [-1,1]: #왼쪽, 오른쪽 회전
                if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                    next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                    next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next_pos
#
# rr = [-1, 0, 1]
# rc1 = [1, 2, 1]
# rc2 = [-1, -2, -1]


def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # "최단 거리"를 재어야 하므로 visited 필요
    robot = {(0,0),(0,1)}
    visited = []
    q = deque([])
    q.append((robot,0))
    visited.append(robot)
    while q:
        pos, time = q.popleft()
        if (n,n) in pos:
            # position에 하나라도 n,n이 있으면
            return time
        for next in get_next_pos(pos, board):
            if next not in visited:
                q.append((next, time+1))
                visited.append(next)
        # r1, r2, t = q.popleft()
        # if ((r1[0] == len(board) - 1 and r1[1] == len(board) - 1) or
        #         (r2[0] == len(board) - 1 and r2[1] == len(board) - 1)):
        #     return t
        # for i in range(4):
        #     n1 = (r1[0] + dr[i], r1[1] + dc[i])
        #     n2 = (r2[0] + dr[i], r2[1] + dc[i])
        #     if (0 <= n1[0] < len(board) and 0 <= n1[1] < len(board)
        #             and 0 <= n2[0] < len(board) and 0 <= n2[1] < len(board)
        #             and (board[n1[0]][n1[1]] != 1 and board[n2[0]][n2[1]] != 1)):
        #         q.append((n1, n2, t + 1))
        #
        # for i in range(3):
        #     n1 = (r1[0] + rr[i], r1[1] + rc1[i])
        #     n2 = (r2[0], r2[1])
        #     if (0 <= n1[0] < len(board) and 0 <= n1[1] < len(board)
        #             and 0 <= n2[0] < len(board) and 0 <= n2[1] < len(board)):
        #         print(n1, n2)
        #         q.append((n1, n2, t + 1))
        #
        # for i in range(3):
        #     n1 = (r1[0], r1[1])
        #     n2 = (r2[0] + rr[i], r2[1] + rc2[i])
        #     if (0 <= n1[0] < len(board) and 0 <= n1[1] < len(board)
        #             and 0 <= n2[0] < len(board) and 0 <= n2[1] < len(board)):
        #         q.append((n1, n2, t + 1))

    return 0