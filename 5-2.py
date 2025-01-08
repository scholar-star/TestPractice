from collections import deque
# python에서 사용하는 양방향 큐인 deque(push, pop이 양방향에서 가능)

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 왼쪽(먼저 들어온 쪽)을 pop

queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순대로 표시
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순대로 표시