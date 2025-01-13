x = int(input())

d = [0]*30001
# def topDown(x):
#     if(x==1):
#         return 1
#     elif(d[x]!=0):
#         return d[x]
#     else:
#         d[x]+=1
#         if(x%5==0):
#             return topDown(x//5)
#         elif(x%3==0):
#             return topDown(x//3)
#         elif(x%2==0):
#             return topDown(x//2)
#         else:
#             return topDown(x-1)
# 누적합 방식 - 보텀업
# topdown보다는 작은 수의 최소 수를 찾아서 가야 하므로
# bottomup이 적합

for i in range(2, x+1):
    d[i] = d[i-1]+1
    # 현재 값에서 1을 빼는 방법의 수
    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i], d[i//5]+1)
    # 호출 횟수를 1번 더함
print(d[x])