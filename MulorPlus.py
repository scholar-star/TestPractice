ls = [int(si) for si in input()]
total = ls[0]

for i in range(1, len(ls)):
    if total+ls[i] > total*ls[i]:
        total += ls[i]
    else:
        total *= ls[i]

print(total)