# def solution(n, build_frame):
#     answer = []
#     # 기둥 : 바닥 위/보의 한쪽 끝 위/다른 기둥 위
#     # 보 : 한쪽 끝부분이 기둥 위 / 양쪽 끝이 다른 보와 연결
#     board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#
#     for b in build_frame:
#         x, y = b[0], (n - b[1])
#         a = b[2]
#         check = b[3]
#
#         print(y, x)
#         if (check == 1):
#             if (a == 0):
#                 if (y == n or board[y][x] == 1):
#                     board[y][x] = 1
#                     board[y - 1][x] = 1
#                     answer.append([b[0], b[1], a])
#                 else:
#                     continue
#             if (a == 1):
#                 if (board[y][x] == 1 or board[y][x + 1] == 1):
#                     board[y][x + 1] = 1
#                     answer.append([b[0], b[1], a])
#                 else:
#                     continue
#         if (check == 0):
#             if (a == 0):
#                 if (board[y + 1][x + 2] == 1):
#                     board[y][x + 1] = 0
#                 else:
#                     continue
#             if (a == 1):
#                 if (board[y - 2][x] == 1):
#                     continue
#                 else:
#                     board[y + 1][x] = 0
#         answer.sort()
#         print(answer)
#
#     return answer

# 좌표 구현 없이 하는 것이 더 직관적
# 구현이라고 해서 좌표를 쓰는 것이 능사는 아니다.

def conform(plan):
    for x,y,a in plan:
        if(a==0): # 기둥일때
            if(y==0 or ([x-1,y,1] in plan) or ([x,y-1,0] in plan)): # 바닥 / 현재 위치 밑 기둥, 옆쪽에 보
                continue
            else:
                return False
        if(a==1): # 보일때
            if((([x-1,y,1] in plan) and ([x+1, y,1] in plan)) or ([x,y-1,0] in plan) or
            [x+1, y-1, 0] in plan): # 현재 위치와 오른쪽 밑에 기둥 // 양쪽 끝 모두 보 존재
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for b in build_frame:
        x,y,a,check = b
        if check==0: #삭제
            answer.remove([x,y,a])
            if(not conform(answer)):
                answer.append([x,y,a])
        if check==1: #설치
            answer.append([x,y,a])
            if(not conform(answer)):
                answer.remove([x,y,a])
    answer.sort()
    return answer