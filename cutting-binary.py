import sys

n,m = tuple(map(int, sys.stdin.readline().split()))
rice_cakes = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(rice_cakes)

while start<=end:
    mid = (start+end)//2
    cutted = [(rice_cake-mid) if (rice_cake>mid) else 0 for rice_cake in rice_cakes]
    # comprehensive list (조건부) :
    # [r if (조건) else 0 for r in range(10)]
    # 조건에 부합하면 r, 아니면 0을 저장

    if(sum(cutted)==m):
        print(mid)
        break
    elif(sum(cutted)>m):
        start = mid+1
    else:
        end = mid-1