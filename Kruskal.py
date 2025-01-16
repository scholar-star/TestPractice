def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [i for i in range(v+1)]

edges = []
result = 0 # 최종 비용

for _ in range(e):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: x[2])

for edge in edges:
    a, b, cost = edge
    if(find_parent(parent,a)!=find_parent(parent,b)):
        union_parent(parent, a, b)
        result += cost

print(result)
