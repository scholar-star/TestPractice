import sys

n,m = tuple(map(int, sys.stdin.readline().split()))
heights = list(map(int, sys.stdin.readline().split()))

for h in range(max(heights),-1,-1):
    lengths = []
    for l in heights:
        if l > h:
            lengths.append(l-h)
        else:
            lengths.append(0)

    if(sum(lengths)==m):
        print(h)
        break