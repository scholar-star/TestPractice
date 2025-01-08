def dfs(graph, v, visited):
    visited[v-1] = True # 처음 노드 방문처리
    print(v, end=' ')
    for i in graph[v-1]: # graph와 인접한 node 방문
        if not visited[i-1]:
            dfs(graph, i ,visited) # 재귀 사용
            # 방문 가능한 것을 바탕으로 더욱 깊게 내려간다.

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

dfs(graph, 1, visited)
# 1을 시작노드로 하여 시작
