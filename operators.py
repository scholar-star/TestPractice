from collections import deque
from copy import deepcopy

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
data = []

for i in range(len(operators)):
    if(operators[i]!=0):
        data.append((0, nums[0], i, operators))

print(data)
# BFS
maximum = 0
minimum = 1000000001
q = deque(data)
while q:
    num_index, calc, operator, opers = q.popleft()
    op = deepcopy(opers) # operator 그대로 = -> 참조
    # 반드시 깊은 복사 필요(copy.deepcopy(l))
    if(operator == 0):
        cal = calc + nums[num_index+1]
    if (operator == 1):
        cal = calc - nums[num_index + 1]
    if (operator == 2):
        cal = calc * nums[num_index + 1]
    if (operator == 3):
         cal = int(calc / nums[num_index + 1]) # int형
    op[operator] -= 1

    print(op, cal)
    if(op == [0 for _ in range(len(op))]): # 마지막 node에 대해서 값을 비교
        # 연산자를 다 넣었을 때 비교
        maximum = max(maximum, cal)
        minimum = min(minimum, cal)

    for i in range(len(opers)):
        if(op[i]>0):
            q.append((num_index+1, cal, i, op))

print(maximum)
print(minimum)
