def check(board): # 들어맞는지 check하는 함수
    lock_len = len(board)//3
    for i in range(lock_len, 2*lock_len):
        for j in range(lock_len, 2*lock_len):
            if(board[i][j]==0): # 모두 1이 아닐 경우
                return False
    return True

# 함수를 사용하면 가독성이 오르고 코드 복잡성을 줄일 수 있다.

# 회전규칙
def rotation(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0*m] for i in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j] # 회전규칙 : 열을 행으로 바꾸고, 열은 전체 행 길이에서 (행+1)을 뺀 것.
    return result

def solution(key, lock):
    board = [[0 for j in range(3*len(lock))] for i in range(3*len(lock))]
    # 보완점 : board의 크기를 lock보다 3배 이상 늘려보자

    for i in range(len(lock),2*len(lock)):
        for j in range(len(lock), 2*len(lock)):
            board[i][j] = lock[i-len(lock)][j-len(lock)]

    for i in range(1, 5):
        if (i == 1):
            rot = [[key[j][k] for j in range(len(key) - 1, -1, -1)] for k in range(len(key))]
    for j in range(len(board)-len(key)+1):
         for k in range(len(board)-len(key)+1):
             for m in range(len(key)):
                 for n in range(len(key)):
                     board[j][k]+= key[m][n]
             if(check(board)):
                 return True
             else:
                 board[j][k] -= key[m][n] # 들어맞지 않는다면 다시 원상복구

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))