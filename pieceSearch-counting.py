# 계수정렬로 계산
import sys

n = int(input())
array = [0]*1000001

for i in list(map(int, sys.stdin.readline().rstrip().split())):
    array[i] += 1

m = int(input())
x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x:
    if array[i] == 1:
        print('yes',end=' ')
    else:
        print('no', end=' ')