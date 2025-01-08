stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 제일 마지막 원소를 pop

stack.append(1)
stack.append(4)
stack.pop()
# [5 2 3 1]

print(stack) # 최하단부터
print(stack[::-1]) # 최상단부터

