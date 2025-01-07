chessLoc = input()
row = ord(chessLoc[0]) - 96
col = int(chessLoc[1])

steps = [(-2, -1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-1,2)]
# knight step으로 가능한 방향을 미리 적어놓음.
count = 0
for s in steps:
    if(s[0]+row >= 1 and s[0]+row <=8 and s[1]+col >= 1 and s[1]+col <= 8):
        count+=1

print(count)
# if(row+2 <= 8):
#     if(col+1 <= 8):
#         count+=1
#     if(col-1 >= 1):
#         count+=1
#
# if(row-2 >= 1):
#     if(col+1 <= 8):
#         count+=1
#     if(col-1 >= 1):
#         count+=1
#
# if(col+2 <= 8):
#     if(row+1 <= 8):
#         count+=1
#     if(row-1 >= 1):
#         count+=1
#
# if(col-2 >= 1):
#     if(row+1 <= 8):
#         count+=1
#     if(row-1 >= 1):
#         count+=1
#
# print(count)
