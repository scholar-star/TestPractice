n, m, k = tuple(map(int, input().split()))
num_list = list(map(int, input().split()))

total = 0
limit = 0

num_list.sort()
for i in range(m):
    if(limit==k):
        total+=num_list[len(num_list)-2]
        limit = 0
    else:
        total += num_list[len(num_list)-1]
        limit += 1

print(total)
