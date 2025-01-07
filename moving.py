n = int(input())
directions = input().split()
loc = [1,1]

for direction in directions:
    if(direction == 'L' and loc[1]-1>=1):
        loc[1]-=1
    if(direction == 'R' and loc[1]+1<=n):
        loc[1]+=1
    if(direction == 'U' and loc[0]-1>=1):
        loc[0]-=1
    if(direction == 'D' and loc[0]+1<=n):
        loc[0]+=1

print(loc[0], loc[1])