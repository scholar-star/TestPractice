n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순으로 정렬

result = 0 # 총 그룹 수
count = 0 # 현 그룹의 모험가 수

for i in data:
    count += 1 # 현재 그룹에 모험가 포함
    if count >= i: # 현재 그룹 모험가 수 >= 공포도
        result += 1
        count = 0

# 최소한의 모험가의 수만 그룹을 결성하고, 나머지는 마을에 있게 된다.
print(result)