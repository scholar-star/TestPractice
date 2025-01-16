def find_parent(parent, x):
    # if parent[x]!=x: # x 부모가 x가 아닐 때(root가 아닐 때)
    #     return find_parent(parent, parent[x]) # root로 거슬러 올라감
    # return x
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
        # root까지 갱신
    return parent[x]
    # root까지의 거리가 짧아지므로 검색 시간이 빨라진다.

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # a가 부모
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # vertex, edge(union) 개수 입력
parent = [i for i in range(v+1)]

for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a,b)

print('각 원소가 속한 집합: ',end='')
for i in range(1, v+1):
    print(find_parent(parent, i),end=' ')
print()

print('부모 테이블: ',end='')
for i in range(1, v+1):
    print(parent[i], end=' ')