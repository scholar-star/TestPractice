n,m = map(int, input().split())

l = []
parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if(parent[x]!=x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a,b,c = map(int, input().split())
    l.append((a,b,c))

l.sort(key=lambda x: x[2])

minspanning = []
for ele in l:
    if(find_parent(parent, ele[1]) != find_parent(parent, ele[0])):
        minspanning.append(ele)
        union(parent, ele[1], ele[0])

minspanning.pop(len(minspanning)-1)
# pop하는 이유 : 마을을 2개로 분할하기 위해서
# 집이 1채 이상만 있으면 되므로, 신장 트리를 만들고
# 유지비가 많이 나오는 도로를 끊어버리면 된다.
print(sum([w[2] for w in minspanning]))
