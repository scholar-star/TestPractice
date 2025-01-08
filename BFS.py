from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # deque([start]) : start를 넣고 시작
    visited[start-1] = True
    while queue: # 비면 null
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v-1]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = True

graph = [
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)
bfs(graph, 1, visited)