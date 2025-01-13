n,k = tuple(map(int, input().split()))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort()

for i in range(k):
    if(list1[i] > list2[n-1-i]):
        continue
    else:
        list1[i], list2[n-1-i] = list2[n-1-i], list[i]

print(sum(list1))