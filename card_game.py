n,m = tuple(map(int, input().split()))
cards = []
mins = []

for _ in range(n):
    l = list(map(int, input().split()))
    cards.append(l)
    mins.append(min(l))

print(max(mins))