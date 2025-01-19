from copy import copy
s=input()
l = [int(sl) for sl in s]

# count = 0
# if l.count(0) > l.count(1):
#     while(l.count(0)!=len(l)):
#         mins = []
#         for i in range(len(l)):
#             for j in range(0,len(l)-i, i):
#                 li = copy.deepcopy(l)
#                 li[j:j+i] = [abs(1-k) for k in l[j:j+i]]
#                 mins.append(li)

count0 = 0 # 0들의 묶음 개수
count1 = 0 # 1들의 묶음 개수

if l[0]==1:
    count0 += 1
else:
    count1 += 1

for i in range(len(l)-1):
    if l[i]!=l[i+1]: # 연속된 카드 장들만 뒤집는 횟수 계산(연속하지 않은 지점까지)
        if l[i+1]==1:
            count0 += 1 # 0이 연속한 묶음 추가
        else:
            count1 += 1 # 1이 연속한 묶음 추가

print(min(count0,count1)) # 더 작은 쪽을 선택



