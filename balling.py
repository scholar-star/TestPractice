n,m = map(int, input().split())
k = list(map(int, input().split()))

s = [se for se in k if se!=max(k)]
k.sort()

count = 0
for ele in s:
    for ks in k:
        if ks > ele:
            count += 1

print(count)