import sys
from time import time

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid]==target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
pieces = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
requests = list(map(int, sys.stdin.readline().rstrip().split()))

pieces.sort()
result = []
for r in requests:
    result.append(binary_search(pieces, r, 0, n-1))

for res in result:
    if(res==True):
        print("yes", end=' ')
    else:
        print("no", end=' ')
