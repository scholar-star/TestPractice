# set 이용하여 구하기
import sys

n = int(input())
array = set(map(int, sys.stdin.readline().rstrip().split()))
# map으로 int화 시킨 것을 set으로 변환
# set의 경우 array에서 element 수를 감소시킨다

m = int(input())
x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
