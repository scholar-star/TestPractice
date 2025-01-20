n = int(input())
l = list(map(int, input().split()))
l.sort() # 작은 동전 단위부터 시작

target = 1
for x in data:
    if target < x: # target이 현재 가리키는 data의 원소보다 작을 때(현재까지 더한 값 < data의 원소)
        break;
    target += x # x를 더하여 가능범위를 넓힌다(target + x -> x ~ x+target까지 가능)