n,m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n+1)]
for i in range(m):
    s,a,b = map(int, input().split())
    if(s==0):
        union(parent, a, b)
    else:
        if(find_parent(parent, a)==find_parent(parent, b)):
            print("YES")
        else:
            print("NO")