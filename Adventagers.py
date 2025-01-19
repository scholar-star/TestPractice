n = int(input())
l = list(map(int, input().split()))

groups = []
while l!=[]:
    s = max(l)
    if s > len(l):
        break

    l.sort()
    g = []
    for c in range(s):
        g.append(l.pop())
    groups.append(g)

# 최대한의 모험가를 파티에 넣는 방법

print(len(groups))