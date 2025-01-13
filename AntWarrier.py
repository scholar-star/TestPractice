from debugpy.common.json import array

n = int(input())
meals = list(map(int, input().split()))

d = [0]*100

# def topDown(l):
#     if(l==None):
#         return 0
#     max_index = l.index(max(l))
#     if (max_index!=0):
#         sub1 = l[:max_index]
#     if(max_index!=len(l)-1):
#         sub2 = l[max_index+1:]
#     sub1_max_index = sub1.index(max(sub1))
#     sub2_max_index = sub2.index(max(sub2))
#     if(abs(sub1_max_index-max_index)==1):
#         return 0
#     if(abs(sub2_max_index-max_index)==1):
#         return 0
#
#     if(d[max_index]!=0):
#         return d[max_index]
#
#     d[max_index] += meals[max_index]
#     return topDown(sub1)+topDown(sub2)+d[max_index]

# dp에서는 d[i-3]이하에 대해 최적의 해를 구할 경우
# d[i-1], d[i-2]를 구하는 과정에서 고려되었기 때문에 - CSP
# 굳이 구할 필요가 없다(메모이제이션)
# ai = max(ai-1, ai-2+ki), k는 현재지점 식량

d[0] = meals[0]
d[1] = max(meals[0], meals[1]) # [k0, k1]
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+meals[i])

print(d[n-1])



