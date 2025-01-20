n,m = map(int, input().split())
data = list(map(int, input().split()))

array = [0]*11 # 볼링공의 개수가 얼만지 세놓은 배열
# 볼링공 번호 수는 10개로 한정

for x in data:
    array[x]+=1

result = 0
for i in range(1, m+1):
    n -= array[i] # 무게가 같은 것의 볼링공은 제외한다
    result += array[i]*n # 제외하고 남은 볼링공과 그 개수에 대한 경우의 수를 곱해 result에 더한다.
    # 숫자 위치가 바뀌는 것은 신경쓰지 않는다.
print(result)