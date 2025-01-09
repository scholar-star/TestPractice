from collections import deque
import sys

n,m = tuple(map(int, input().split()))
board = [list(map(int, list(map(int, sys.stdin.readline().rstrip())))) for _ in range(n)]
# import sys
# sys.std.readline() : 한 줄의 것을 읽음(개행문자 포함)
# rstrip() : 오른쪽 문자(개행문자)를 벗김
# 문자열의 list화 : 문자 개별로의 list로 변환

# def bfs(start, board):
#     queue = deque([start])
#     board[start[0]][start[1]] = 2
#     actions = [(start[0]+d[0], start[1]+d[1]) for d in [(-1, 0),(1, 0),(0, -1),(0, 1)]
#                if(start[0]+d[0]<=4 and start[0]+d[0]>=0 and start[1]+d[1]<=4 and start[1]+d[1]>=0)]
#     print(actions)
#
#     for a in actions:
#         if(board[a[0]][a[1]]==0):
#             queue.append(a)
#     queue.popleft()
# dfs일때 더 쉽게 풀린다.(갈래 수가 적은 편이기 때문)

# board는 전역변수이므로 따로 매개변수화 하지않고 사용 가능.

def dfs(i, j):
    # 재귀를 사용할 경우 종료조건 지정(필수)
    if(i>n-1 or i<0 or j>m-1 or j<0):
        return False # 지정된 칸을 넘어갈경우 false 처리(그리고 여기서 종료)

    if(board[i][j]==0):
        board[i][j]=1
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1) # 모든 방향에서 깊이 탐색
        return True # start(i,j)가 0이면 True
    return False #아니면 False

count = 0
for i in range(n):
    for j in range(m):
        if(dfs(i,j)):
            count += 1

print(count)