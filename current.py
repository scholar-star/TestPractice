n,m = tuple(map(int,input().split()))
vs = [int(input()) for _ in range(n)]

d = [10001]*(m+1)
# 가질 수 없는 화폐가치로 초기화
# 그렇다면, 밑 초기화 과정은 필요없음.

# for i in range(len(d)):
#     if(d[i]<min(vs)):
#         d[i] = -1
#     else:
#         d[i]

d[0]=0 # 0이 될 경우에는 min으로 비교할 때 밖에 없으므로 0이 되어야 제대로 된 비교가 가능하다.
# "화폐를 하나도 사용하지 않는 경우"로 상정(다른 것은 화폐가 있어도 만들 수 없음.)
for i in range(n):
    for j in range(vs[i], m+1): # 점층적으로 vs[i]에 대하여 가능한 것들에 대해 누적해간다.
        if d[j-vs[i]]!=10001: # 불가능한 화폐가치가 아니라면
            # 접근 자체는 나쁘지 않았음
            d[j] = min(d[j-vs[i]]+1,d[j]) # 본래 값과 비교, 최소인 쪽을 넣는다.

if (d[m]==10001):
    print(-1)
else:
    print(d[m])





